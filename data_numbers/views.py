""" File that conatinas the controller of MVC,
the code controlling the business logic of the application. """
import django.core.handlers.wsgi
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect, render
from django.template import loader

from data_numbers.forms import ModifyUsernameForm, UserRegistrationForm


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


# def edit_username(request):
#     if request.method == "POST":
#         user = request.user
#         new_username = request.POST["username"]
#         user.username = new_username
#         user.save()
#         return redirect("profile")
#     else:
#         print(request)
#         return render(request, "profile.html", {})
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
