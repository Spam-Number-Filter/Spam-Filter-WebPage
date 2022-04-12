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
    And There is no logged in user

  Scenario: User logouts from the website and there's no logged in user
    Given An user is not logged in the website
    When I try to logout
    Then I'm viewing that there's no log out button
    And I can't click on the button