Feature: Delete post
  In order to hace controll of my posts
  As a user
  I want to be able to delete my posts

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And There is a category "spam"
    And An user is logged in the website
    And I am on the create post page
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      | Post title  | Post message  | 47               | 111223344        |
    And I choose Category "Spam"
    And I press "Post"

  Scenario: Delete a post
    When I click on the delete button
    Then I sould be redirected to the home page
    And I go to trendy
    Then I shouldn't see my post

