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


@when('I press "modify_user" button')
def modify_user_action(context):
    context.browser.find_by_id("modify_user").click()


@then(
    'I\'m viewing a page with the form "new_username" where i can enter the new username'
)
def viewing_account_button(context):
    assert context.browser.is_element_present_by_id("new_username")


@step('I\'m viewing the submit button "modify_user_submit"')
def viewing_submit_button(context):
    assert context.browser.is_element_present_by_id("modify_user_submit")


@step('I fill the "new_username" form with the "MyNewUsername"')
def fill_form(context):
    context.browser.fill("new_username", "modified_username")


@step('I press "modify_user_submit" button')
def submit_changes(context):
    context.browser.find_by_id("modify_user_submit").click()
