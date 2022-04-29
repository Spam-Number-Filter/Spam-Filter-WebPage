# Created by roger at 29/4/22
Feature: modify user
  In order to modify an user from the website
  As a user
  I want to log modify the current user

    Background: There's an user registered
      Given Exists a user "user" with password "password"


  Scenario: User modifies username
    Given An user is logged in the website
    When I press "modify_user" button
    Then I'm viewing a page with the form "new_username" where i can enter the new username
    And I'm viewing the submit button "modify_user_submit"
    And I fill the "new_username" form with the "MyNewUsername"
    And I press "modify_user_submit" button
