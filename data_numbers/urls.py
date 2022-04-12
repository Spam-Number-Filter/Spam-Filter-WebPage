"""" Module that contains a lsit of URL patterns
and which view should be run when they are requested. """
from django.urls import include, path
from django.views.generic import TemplateView

from data_numbers.views import login_user, register_user

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "accounts/profile/",
        TemplateView.as_view(template_name="profile.html"),
        name="profile",
    ),
]
