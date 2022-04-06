from django.contrib import admin
from data_numbers.models import Telephone, Post, Comment, Category, VoteCategory

admin.site.register(Telephone)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(VoteCategory)
