Feature: See user profile
  In order to see my profile, with my name, email and password
  As a user
  I want to see the user profile

  Background: There is a registered user with username "admin" and password "admin"
    Given Existing user "admin" with password "admin"

  Scenario: See user profile if user is logged in
    Given I am logged in as "admin" with password "admin"
    When I go to the user profile
    Then I should see the user profile

  Scenario: See user profile if user is not logged in
    Given I am not logged in
    When I go to the user profile url
    Then There should be a error asking for me to login