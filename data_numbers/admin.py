""" Module that contains all the data entities to be registered by the administrator."""
from django.contrib import admin

from data_numbers.models import Category, Comment, Post, Telephone

admin.site.register(Telephone)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
