Feature: Like post
  In order to engage posts
  As a user
  I want to be able to like a post

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

  Scenario: Like a post
    When I click on like button
    Then I should be redirected to the same post page
    And I go to trendy
    Then I should see one more like on the post

  Scenario: Unlike a post
    When I click on like button
    Then I should be redirected to the same post page
    When I click on like button
    Then I should be redirected to the same post page
    And I go to trendy
    Then I should see the post has not likes