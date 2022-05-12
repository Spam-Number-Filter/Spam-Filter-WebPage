""" File that contains all data entities of our project. """
from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.
from django.db.models import Model
from django.urls import reverse

NAME_MAX_LENGTH = 50
PASSWORD_MAX_LENGTH = 20
EMAIL_MAX_LENGTH = 100
MAX_CATEGORY_LENGTH = 20
TITLE_MAX_LENGTH = 30


class Telephone(Model):
    """Telephone model."""

    telephone_id = models.AutoField(primary_key=True)
    phone = models.IntegerField()
    prefix = models.IntegerField()

    class Meta:
        unique_together = ("phone", "prefix")


class Category(Model):
    """Category model, from a post."""

    type = models.CharField(max_length=MAX_CATEGORY_LENGTH, primary_key=True)


class Post(Model):
    """Post model."""

    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    telephone = models.ForeignKey(Telephone, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        AUTH_USER_MODEL, related_name="tel_posts", blank=True
    )

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(Model):
    """Comment model, from a post."""

    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
