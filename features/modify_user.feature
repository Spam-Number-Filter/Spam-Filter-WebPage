Feature: modify user
  In order to modify an user from the website
  As a user
  I want to modify the current user data

  Background: There's an user registered
    Given Exists a user "user1" with password "password1"


  Scenario: User modifies username
    Given An user is logged in the website.
    When I press the button "account"
    When I press "edit_username_button" button
    Then I'm viewing a page with the text input "username" where i can enter the new username
    And I'm viewing the submit button "submit_button"
    And I fill the "username" input with the new username "modified_username"
    And I press "submit_button" button


