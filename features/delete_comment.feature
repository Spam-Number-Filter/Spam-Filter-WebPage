Feature: Delete comment
  In order to have control of my comments
  As a user
  I want to be able to delete my comments

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And There is a category "spam"
    And An user is logged in the website
    And I am on the create post page
    When I create a post
      | title      | message      | telephone_prefix | telephone_number |
      | Post title | Post message | 47               | 111223344        |
    And I choose Category "Spam"
    And I press "Post"

  Scenario: Delete my own comment
    Given I write a new comment
    When I click on the delete comment button
    Then I souldn't see my comment anymore

  Scenario: Try to delete other user's comment
    Given I logout
    And I login as user "admin" with password "admin"
    And I go to the post
    And I add a comment to the first post
    And I logout
    And I log in as "user" with password "password"
    And I go to the post
    Then I shouldn't see a delete button inside admin's comment

