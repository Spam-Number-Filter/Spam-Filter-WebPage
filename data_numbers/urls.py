"""" Module that contains a lsit of URL patterns
and which view should be run when they are requested. """
from django.urls import include, path
from django.views.generic import TemplateView

from data_numbers.views import login_user

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", login_user, name="login"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
