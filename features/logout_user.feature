Feature: Valid Logout User
  In order to logout an user from the website
  As a user
  I want to logout to leave the webpage

  Background: There's an user registered
    Given Exists a user "user" with password "password"

  Scenario: User logouts from the website
    Given An user is logged in the website
    When I logout
    Then I'm viewing that "account" button is not appearing anymore
    And I'm viewing the login button

  Scenario: User can't logout from the website
    Then There is no log out button