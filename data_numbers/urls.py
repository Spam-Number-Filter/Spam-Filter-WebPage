"""" Module that contains a lsit of URL patterns
and which view should be run when they are requested. """
from django.urls import include, path
from django.views.generic import TemplateView

from data_numbers.views import (
    PostCreate,
    PostDetail,
    PostUpdateView,
    add_comment,
    delete_comment,
    delete_posts,
    edit_username,
    get_numbers,
    get_prefixes,
    login_user,
    register_user,
    search_numbers,
    submit_like,
    trendy_posts,
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
    path("post/create/", PostCreate.as_view(), name="post_create"),
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
    path("api/search_number/", search_numbers, name="search_numbers"),
    path("post/<int:post_id>/api/delete_post/", delete_posts, name="delete_posts"),
    path(
        "post/<int:post_id>/api/submit_like/<int:user_id>/",
        submit_like,
        name="submit_like",
    ),
    # Post details
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path(
        "trendy/",
        trendy_posts,
        name="trendy",
    ),
    path("post/<int:post_id>/api/add_comment/", add_comment, name="add_comment"),
    path(
        "post/api/delete_comment/<int:comment_id>/",
        delete_comment,
        name="delete_comment",
    ),
    path("post/edit/<int:pk>/", PostUpdateView.as_view(), name="post_update_form"),
]
