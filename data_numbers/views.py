""" File that conatinas the controller of MVC,
the code controlling the business logic of the application. """
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect, render
from django.template import loader


def index(request):
    """Controller of the index page."""
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.success(request, ("There was an error logging in"))
            return redirect("login")
    else:
        print(request)
        return render(request, "registration/login.html", {})
