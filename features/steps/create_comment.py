from behave import given, step, then, when
from django.contrib.auth.models import User

from data_numbers.models import Category, Post, Telephone
from features.steps.login_user import click_login_button, login


@given('Exists a user "user2" with password "password2"')
def exists_user(context):
    user = context.db.create_user(username="user2", password="password2")
    user.save()


@given('Exists a post with post_id "1"')
def exists_a_post(context):
    telephone = Telephone()
    telephone.prefix = 34
    telephone.phone = 123412345
    telephone.telephone_id = 1
    telephone.save()
    post = Post()
    post.post_id = 1
    post.message = "test message"
    post.telephone = telephone
    post.user_id = User.objects.get(username="user2")
    post.category = Category.objects.get(type="spam")
    post.save()


@step('I log in as "user2" with password "password2"')
def logged_user(context):
    login(context, "user2", "password2")
    click_login_button(context)


@step('I am on the post "1" page')
def visit_post(context):
    context.browser.visit(context.get_url("/posts/1"))


@when("I click on the comment")
def step_impl(context):
    context.browser.find_by_name("message").first.click()


@when("I write a comment")
def write_comment(context):
    message = context.browser.find_by_name("message").first
    message.fill("new message")


@step('I press "Submit"')
def press_submit(context):
    context.browser.find_by_id("submit-button").click()


@then('I should see the comment "comment1"')
def assert_comment_exists(context):
    # TODO: it will fail until Pablo fixes the problem of creating a comment with firefox
    context.browser.visit(context.get_url("/posts/1"))
    assert context.browser.is_element_present_by_id("comment-div")
