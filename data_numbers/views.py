""" File that contains the controller of MVC,
the code controlling the business logic of the application. """
import json

import django.core.handlers.wsgi
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import CreateView, DetailView

from data_numbers.forms import ModifyUsernameForm, PostForm, UserRegistrationForm
from data_numbers.models import Post, Telephone
from data_numbers.forms import ModifyUsernameForm, UserRegistrationForm
from data_numbers.models import Post


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
            messages.error(request, ("There was an error logging in"))
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
    form_class = PostForm
    template_name = "post/post_creation.html"

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        form.instance.telephone = self.getPostCreationTelephone(form)
        return super(PostCreate, self).form_valid(form)

    def getPostCreationTelephone(self, form):
        prefix = form.cleaned_data["telephone_prefix"]
        number = form.cleaned_data["telephone_number"]
        telephone = Telephone.objects.create(prefix=prefix, phone=number)
        return Telephone.objects.get(telephone_id=telephone.telephone_id)


class PostDetail(DetailView):
    model = Post
    template_name = "post/post_detail.html"


def get_prefixes(request):
    try:
        prefix = request.GET["prefix"]
        prefixes = Telephone.objects.filter(prefix__startswith=prefix)
        return HttpResponse(json.dumps([p.prefix for p in prefixes]))
    except Exception as e:
        return HttpResponse(f"Error: ${e}")


def get_numbers(request):
    try:
        number = request.GET["number"]
        numbers = Telephone.objects.filter(phone__startswith=number)
        return HttpResponse(json.dumps([p.phone for p in numbers]))
    except Exception as e:
        return HttpResponse(f"Error: ${e}")


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
