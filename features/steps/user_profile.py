from behave import given, when, then


@given('Existing user "admin" with password "admin"')
def create_user(context):
    user = context.db.create_user(username="admin", password="admin")
    user.save()


@given('I am logged in as "admin" with password "admin"')
def login_user_admin_admin(context):
    login(context, "admin", "admin")


def login(context, username, password):
    context.browser.visit(context.get_url("/accounts/login"))
    context.browser.fill("username", username)
    context.browser.fill("password", password)
    form = context.browser.find_by_tag("form").first
    form.find_by_value("login").click()


@when("I go to the user profile")
def click_user_profile(context):
    context.browser.find_by_id("account").click()


@then("I should see the user profile")
def check_user_profile(context):
    assert context.browser.url == context.get_url("/accounts/profile/")


@given("I am not logged in")
def user_not_logged(context):
    context.browser.visit(context.get_url("/accounts/logout"))


@when("I go to the user profile url")
def insert_profile_url(context):
    context.browser.visit(context.get_url("/accounts/profile"))


@then("There should be a error asking for me to login")
def check_error(context):
    assert context.browser.is_text_present("Log in before accessing your account")
