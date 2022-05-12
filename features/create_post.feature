Feature: Create post
  In order to inform of a spam number
  As a user
  I want to crete a post together with its phone number and category

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And I log in as "user" with password "password"
    And I am on the create post page

  Scenario: Create a post without assigning a category
    When I create a post
      | title       | message       | telephone_prefix | telephone_number |
      | Post title  | Post message  | 43               | 111223344        |
    And I press "Post"
#    Then I should see an error message

  Scenario: Create a post with an already existing phone number
    # Enter steps here

  Scenario: Create a post without a telephone number
    # Enter steps here

  Scenario: Create a post without a telephone prefix
    # Enter steps here

  Scenario: Create a post with a non existing phone number
    # Enter steps here