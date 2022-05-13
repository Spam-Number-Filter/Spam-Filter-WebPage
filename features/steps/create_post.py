from behave import step, then, when

from data_numbers.models import Category


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


@step('I choose Category "Spam"')
def choose_spam(context):
    context.browser.select("selector", "Spam")


@then("I sould see the post details")
def check_is_on_post_details_as_owner(context):
    assert context.browser.is_text_present("Home")


@step('There is a "Spam" category created')
def step_impl(context):
    Category.objects.create(type="Spam")
    # category = Category.objects.get(type="Spam")
