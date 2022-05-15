Feature: Modify post
  In order to change some post data
  As a user
  I want to be able to modify a post title and/or message

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

  Scenario: Error - modify just the title
    Given I am on the post page
    When I click on the modify button
    And I fill in "title" with "New title"
      | title     |
      | New title |
    And I click on the "Submit" button
    Then I should see the post edit page
    And There should be no input in any field


  Scenario: Error - modify just the message
    Given I am on the post page
    When I click on the modify button
    And I fill in "message" with "New message"
      | message     |
      | New message |
    And I click on the "Submit" button
    Then I should see the post edit page
    And There should be no input in any field


  Scenario: Correct - modify both title and message
    Given I am on the post page
    When I click on the modify button
    And I fill in "title" with "New title"
      | title     |
      | New title |
    And I fill in "message" with "New message"
      | message     |
      | New message |
    And I click on the "Submit" button
    Then I should the post with the new title and message
