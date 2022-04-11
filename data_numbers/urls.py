"""" Module that contains a lsit of URL patterns
and which view should be run when they are requested. """
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
