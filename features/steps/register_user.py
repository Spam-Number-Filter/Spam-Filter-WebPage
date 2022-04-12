from behave import given, step, use_step_matcher, when
from django.contrib.auth.models import User

use_step_matcher("re")


@given('Exists a user with username "user" and password "password"')
def create_user(context):
    # Create a user with username "user" and password "password"
    user = User.objects.create_user(username="user", password="password")
    user.save()


@given("I am on the register page")
def render_register_page(context):
    # Go to the register page
    context.browser.visit(context.get_url("register"))


@when('I fill in "username" with "user"')
def fill_username(context):
    raise NotImplementedError('STEP: When I fill in "username" with "user"')


@step('I fill in "password" with "password"')
def fill_password(context):
    raise NotImplementedError('STEP: And I fill in "password" with "password"')
