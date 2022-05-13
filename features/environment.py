from django.contrib.auth.models import User
from splinter.browser import Browser


def before_all(context):
    context.browser = Browser("firefox", headless=False)
    context.db = User.objects


def after_all(context):
    context.browser.quit()
    context.browser = None
