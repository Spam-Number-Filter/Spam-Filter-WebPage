from behave import given


@given('Exists a user "user" with password "password"')
def exists_user(context):
    user = context.db.create_user(username="admin", password="admin")
    user.save()


@given("An user is logged in the website")
def logged_user(context):
    context.browser.visit(context.get_url("/accounts/login/"))
    form = context.browser.find_by_tag("form").first
    context.browser.fill("username", "admin")
    context.browser.fill("password", "admin")
    form.find_by_value("login").first.click()
