from behave import given, step, then, when
from login_user import click_login_button, login


@given('Exists a user "user1" with password "password1"')
def exists_user(context):
    user = context.db.create_user(username="user1", password="password1")
    user.save()


@given("An user is logged in the website.")
def logged_user(context):
    login(context, "user1", "password1")
    click_login_button(context)


@when('I press the button "account"')
def acces_account_page(context):
    context.browser.find_by_id("account").click()


@when('I press "edit_username_button" button')
def modify_user_action(context):
    context.browser.find_by_id("edit_username_button").click()


@then(
    'I\'m viewing a page with the text input "username" where i can enter the new username'
)
def viewing_account_button(context):
    assert context.browser.is_element_present_by_id("username")


@step('I\'m viewing the submit button "submit_button"')
def viewing_submit_button(context):
    assert context.browser.is_element_present_by_id("submit_button")


@step('I fill the "username" input with the new username "modified_username"')
def fill_form(context):
    context.browser.fill("username", "modified_username")


@step('I press "submit_button" button')
def submit_changes(context):
    context.browser.find_by_id("submit_button").click()
