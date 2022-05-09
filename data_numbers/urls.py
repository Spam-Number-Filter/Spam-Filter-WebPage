"""" Module that contains a lsit of URL patterns
and which view should be run when they are requested. """
from django.urls import include, path
from django.views.generic import TemplateView
from data_numbers.views import (
    get_numbers,
    get_prefixes,
    PostCreate,
    PostDetail,
    edit_username,
    login_user,
    register_user,
)

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
    path(
        "accounts/profile/edit-profile/",
        TemplateView.as_view(template_name="edit_username.html"),
        name="edit_username",
    ),
    path("edit-profile/", edit_username, name="submit_edit_username"),
    path("post/create", PostCreate.as_view(), name="post_create"),
    path(
        "site-policy/privacy/",
        TemplateView.as_view(template_name="privacy.html"),
        name="privacy",
    ),
    path(
        "site-policy/terms/",
        TemplateView.as_view(template_name="terms.html"),
        name="terms",
    ),
    path("api/get_prefixes/", get_prefixes, name="get_prefixes"),
    path("api/get_numbers/", get_numbers, name="get_places"),
    # Post details
    path("posts/<int:pk>", PostDetail.as_view(), name="post_detail"),
    path(
        "trendy/",
        TemplateView.as_view(template_name="trendy.html"),
        name="trendy",
    ),
]
