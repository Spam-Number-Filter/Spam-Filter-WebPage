from behave import step, then, when

from data_numbers.models import Category, Telephone


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
    context.browser.select("selector", "spam")


@then("I sould see the post details")
def check_is_on_post_details_as_owner(context):
    assert context.browser.find_by_id("modify")


@step('There is a telephone number "+34 000112233" created')
def create_telephone(context):
    Telephone.objects.create(prefix="34", phone="000112233")


@step('There is a category "spam"')
def create_spam_category(context):
    try:
        Category.objects.create(type="spam")
    except Exception as e:
        print("Ignoring error {}".format(e))
