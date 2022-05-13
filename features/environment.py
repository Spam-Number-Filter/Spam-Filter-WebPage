from django.contrib.auth.models import User
from splinter.browser import Browser

from data_numbers.models import Category


def before_all(context):
    context.browser = Browser("firefox", headless=True)
    context.db = User.objects
    context.db_categories = Category.objects


def after_all(context):
    context.browser.quit()
    context.browser = None
