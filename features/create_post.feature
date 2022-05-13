Feature: Create post
  In order to inform of a spam number
  As a user
  I want to crete a post together with its phone number and category

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And There is a category "spam"
    And There is a telephone number "+34 000112233" created
    And An user is logged in the website
    And I am on the create post page

  Scenario: Correctly create a post
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      | Post title  | Post message  | 47               | 111223344        |
    And I choose Category "Spam"
    And I press "Post"
    Then I sould see the post details
#
  Scenario: Create a post without assigning a category
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      | Post title  | Post message  | 43               | 111223344        |
    And I press "Post"
    Then I should see an error message
#
  Scenario: Create a post without a title
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      |             | Post message  | 43               | 111223344        |
    And I choose Category "Spam"
    And I press "Post"
    Then I should see an error message

  Scenario: Create a post with an already existing phone number
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      | Post title  | Post message  | 34               | 000112233        |
    And I choose Category "Spam"
    And I press "Post"
    Then I should see an error message

  Scenario: Create a post without a telephone number
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      | Post title  | Post message  | 34               |                     |
    And I choose Category "Spam"
    And I press "Post"
    Then I should see an error message

  Scenario: Create a post without a telephone prefix
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      | Post title  | Post message  |                  | 111223344        |
    And I choose Category "Spam"
    And I press "Post"
    Then I should see an error message

  Scenario: Create a post with a non existing phone number
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      | Post title  | Post message  | 34               | 0001122340000000 |
    And I choose Category "Spam"
    And I press "Post"
    Then I should see an error message
