from behave import given, step, then, use_step_matcher, when
from django.contrib.auth.models import User

use_step_matcher("parse")


@given(
    'Exists a user with username "user", password "password" and email "email@sample.com"'
)
def create_user(context):
    user = User.objects.create_user(
        username="user", password="password", email="email@sample.com"
    )
    user.save()


@given("I am on the register page")
def render_register_page(context):
    context.browser.visit(context.get_url("/register"))


@when("I enter my credentials")
def enter_credentials(context):
    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])


@step('I press "Register"')
def press_register(context):
    form = context.browser.find_by_tag("form").first
    form.find_by_value("signup").click()


@then("I should see I am logged in")
def logged_in(context):
    context.browser.visit(context.get_url("/"))
    assert context.browser.is_element_present_by_id("logout")
