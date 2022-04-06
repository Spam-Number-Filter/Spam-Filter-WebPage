from django.db import models

# Create your models here.
from django.db.models import Model
from django.contrib.auth.models import User

NAME_MAX_LENGTH = 50
PASSWORD_MAX_LENGTH = 20
EMAIL_MAX_LENGTH = 100


class Telephone(Model):
    telephone_id = models.AutoField(primary_key=True)
    phone = models.IntegerField()
    prefix = models.IntegerField()

    class Meta:
        unique_together = (
            "phone",
            "prefix",
        )


TITLE_MAX_LENGTH = 30


class Post(Model):
    post_id = models.AutoField(primary_key=True)
    creation_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    # TODO: Put that on documentation
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    telephone = models.ForeignKey(Telephone, on_delete=models.CASCADE)


class Comment(Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


MAX_CATEGORY_LENGTH = 20


class Category(Model):
    type = models.CharField(max_length=MAX_CATEGORY_LENGTH, primary_key=True)


class VoteCategory(Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
