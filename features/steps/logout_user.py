from behave import given, step, then, when
from login_user import click_login_button, login


@given('Exists a user "user" with password "password"')
def exists_user(context):
    user = context.db.create_user(username="user", password="password")
    user.save()


@given("An user is logged in the website")
def logged_user(context):
    login(context, "user", "password")
    click_login_button(context)


@then('I\'m viewing that "account" button is not appearing anymore')
def viewing_account_button(context):
    assert not context.browser.is_element_present_by_id("account")


@when("I logout")
def logout_action(context):
    context.browser.find_by_id("logout").click()


@then("There is no log out button")
def no_logout_button(context):
    assert not context.browser.is_element_present_by_id("logout")


@step("I'm viewing the login button")
def viewing_login_button(context):
    assert not context.browser.is_element_present_by_id("login")
