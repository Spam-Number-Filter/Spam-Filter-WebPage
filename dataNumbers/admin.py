from django.contrib import admin
from dataNumbers.models import *
from django.apps import apps

# Register your models here.
# models = apps.get_models()
# for model in models:
#     admin.site.register(model)

admin.site.register(Telephone)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(VoteCategory)
