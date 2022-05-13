""" File that contains the controller of MVC,
the code controlling the business logic of the application. """
import json
from typing import Tuple

import django.core.handlers.wsgi
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import CreateView, DetailView, UpdateView

from data_numbers.forms import (
    CommentForm,
    CreatePostForm,
    ModifyUsernameForm,
    UserRegistrationForm,
)
from data_numbers.models import Category, Comment, Post, Telephone
from data_numbers.validation.category_validation import (
    CategoryValidationData,
    valid_category,
)
from data_numbers.validation.number_validation import (
    NumberValidation,
    NumberValidationData,
)
from data_numbers.validation.number_validation_factory import get_number_validation


def index(request):
    """Controller of the index page."""
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def login_user(request: django.core.handlers.wsgi.WSGIRequest):
    print(request)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "There was an error logging in")
            return redirect("login")
    else:
        print(request)
        return render(request, "registration/login.html", {})


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, form.errors)
            return redirect("register")

    form = UserCreationForm
    return render(
        request=request,
        template_name="registration/register.html",
        context={"form": form},
    )


def edit_username(request):
    if request.method == "POST":
        form = ModifyUsernameForm(request.POST)
        if form.is_valid():
            user = request.user
            user.username = form.modify_username()
            user.save()
        else:
            messages.success(request, form.errors)
            return redirect("edit_username")
        return redirect("profile")
    else:
        print(request)
        return render(request, "profile.html", {})


class PostCreate(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "post/post_creation.html"

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        if not self.setPostCategory(form).is_valid:
            return redirect("post_create")
        if not self.setPostNumber(form).is_valid:
            return redirect("post_create")
        return super(PostCreate, self).form_valid(form)

    def setPostCategory(self, form) -> CategoryValidationData:
        category = form.data["selector"]
        validation_result = valid_category(category)
        if not validation_result.is_valid:
            error_message = valid_category(category).error_message
            messages.error(self.request, error_message)
        else:
            form.instance.category = Category.objects.get(type=category)
        return validation_result

    def setPostNumber(self, form) -> NumberValidationData:
        validation_result = PostCreate.get_validator(form).valid_number()
        if not validation_result.is_valid:
            error_message = validation_result.error_message
            messages.error(self.request, error_message)
        else:
            form.instance.user_id = self.request.user
            form.instance.telephone = PostCreate.getPostCreationTelephone(form)
        return validation_result

    @staticmethod
    def get_validator(form) -> NumberValidation:
        prefix, number = PostCreate.get_prefix_and_suffix(form)
        return get_number_validation(prefix, number)

    @staticmethod
    def get_prefix_and_suffix(form) -> Tuple[int, int]:
        return (
            form.data["telephone_prefix"],
            form.data["telephone_number"],
        )

    @staticmethod
    def getPostCreationTelephone(form) -> Telephone:
        prefix = form.data["telephone_prefix"]
        number = form.data["telephone_number"]
        telephone = Telephone.objects.create(prefix=prefix, phone=number)
        return Telephone.objects.get(telephone_id=telephone.telephone_id)


class PostDetail(DetailView):
    model = Post
    template_name = "post/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        all_comments = Comment.objects.all()
        wanted_comments = []
        for comment in all_comments:
            if comment.post_id.post_id == pk:
                wanted_comments.append(comment)
        context["comments"] = wanted_comments
        return context


def get_prefixes(request):
    try:
        prefix = request.GET["prefix"]
        prefixes = Telephone.objects.filter(prefix__startswith=prefix)
        unique_prefixes = list(set([p.prefix for p in prefixes]))
        return HttpResponse(json.dumps(unique_prefixes))
    except Exception as e:
        return HttpResponse(f"Error: ${e}")


def get_numbers(request):
    try:
        number = request.GET["number"]
        numbers = Telephone.objects.filter(phone__startswith=number)
        return HttpResponse(json.dumps([p.phone for p in numbers]))
    except Exception as e:
        return HttpResponse(f"Error: ${e}")


def search_numbers(request):
    if request.method == "GET":
        prefix = request.GET["prefix"]
        number = request.GET["number"]
        try:
            telephone = Telephone.objects.get(prefix=prefix, phone=number)
        except Exception:
            return HttpResponse("/post/create")
        post = Post.objects.get(telephone=telephone)
        return HttpResponse("/posts/" + post.post_id.__str__())
    else:
        return HttpResponse("Error")


def trendy_posts(request):
    all_posts = Post.objects.all()
    ten_trendy_posts = get_trendy_posts(all_posts)
    context = {"ten_trendy_posts": ten_trendy_posts}
    return render(request, "trendy.html", context)


def get_trendy_posts(all_posts):
    trendy_posts_dict = dict()
    for post in all_posts:
        trendy_posts_dict[post.post_id] = post.likes.count()
    trendy_posts_dict = sorted(
        trendy_posts_dict.items(), key=lambda x: x[1], reverse=True
    )[:10]
    return get_posts(trendy_posts_dict)


def get_posts(trendy_posts_dict):
    ten_trendy_posts = []
    for post_id, _ in trendy_posts_dict:
        ten_trendy_posts.append(Post.objects.get(post_id=post_id))
    return ten_trendy_posts


def add_comment(request, pk):
    print("hola")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user.username
            comment = Comment()
            comment.post_id = Post.objects.get(pk=pk)
            comment.user_id = User.objects.get(username=user)
            comment.message = form.get_message()
            comment.save()
        else:
            messages.success(request, form.errors)

        return HttpResponse("/posts/" + str(pk))
    else:
        return HttpResponse("home")


def delete_posts(request, pk):
    post_id = request.POST["post_id"]
    post = Post.objects.get(post_id=post_id)
    post.delete()
    return HttpResponse("/")


def submit_like(request, pk):
    post_id = request.POST["post_id"]
    user_id = request.POST["user_id"]
    post = Post.objects.get(post_id=post_id)
    likes = post.likes.all()
    if remove_if_liked(likes, user_id, post, request):
        return HttpResponse("/posts/" + post_id)
    else:
        return add_like(user_id, post_id, post)


def remove_if_liked(likes, user_id, post, request):
    for user_like in likes:
        if str(request.user.username) == str(user_like):
            post.likes.remove(user_id)
            return True


def add_like(user_id, post_id, post):
    post.likes.add(user_id)
    return HttpResponse("/posts/" + post_id)


class PostUpdateView(UpdateView):
    model = Post
    fields = (
        "title",
        "message",
    )
    template_name = "post/post_update_form.html"
