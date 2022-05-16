Feature: Create a comment on a post
  In order to comment a post
  As a user
  I want to create a comment in a post

  Background: There is a registered user and a post
    Given Exists a user "user" with password "password"
    And There is a category "spam"
    And An user is logged in the website
    And I am on the create post page
    When I create a post
      | title      | message      | telephone_prefix | telephone_number |
      | Post title | Post message | 47               | 111223344        |
    And I choose Category "Spam"
    And I press "Post"


  Scenario: Create comment
    When I click on the comment
    And I write a comment
      | comment                         |
      | Sample comment, liked this post |
    And I press "Submit"
    Then I should see the comment
      | comment                         |
      | Sample comment, liked this post |
    And I should still be on the post page
