from behave import step, when


@step('I log in as "user" with password "password"')
def login_user_user_password(context):
    login(context, "user", "password")


def login(context, username, password):
    context.browser.visit(context.get_url("/accounts/login"))
    context.browser.fill("username", username)
    context.browser.fill("password", password)


@step("I am on the create post page")
def visit_create_post(context):
    context.browser.visit(context.get_url("/post/create"))


@when("I create a post")
def enter_credentials(context):
    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])


@step('I press "Post"')
def press_register(context):
    form = context.browser.find_by_tag("form").first
    form.find_by_value("post").click()
