Feature: Register User
  In order to have an account on the website
  As a user
  I want to create and register a user with the credentials of my choice

  Background: There is a registered user
    Given Exists a user with username "user" and password "password"

  # Register a new user with already taken username
  Scenario: Register a new user with already taken username
    Given I am on the register page
    When I fill in "username" with "user"
    And I fill in "password" with "password"
    And I fill in "password_confirmation" with "password"
    And I press "Register"
    Then I should see "Username has already been taken"

  # Register a new user with an invalid username
  Scenario: Register a new user with an invalid username
    Given I am on the register page
    When I fill in "username" with "user"
    And I fill in "password" with "password"
    And I fill in "password_confirmation" with "password"
    And I press "Register"
    Then I should see "Username is invalid"

  # Register a new user with an invalid password
  Scenario: Register a new user with an invalid password
    Given I am on the register page
    When I fill in "username" with "user"
    And I fill in "password" with "password"
    And I fill in "password_confirmation" with "password"
    And I press "Register"
    Then I should see "Password is too short (minimum is 6 characters)"

  # Register a new user with an invalid password confirmation
  Scenario: Register a new user with an invalid password confirmation
    Given I am on the register page
    When I fill in "username" with "user"
    And I fill in "password" with "password"
    And I fill in "password_confirmation" with "password1"
    And I press "Register"
    Then I should see "Password confirmation doesn't match Password"

  # Register a new user with valid credentials
  Scenario: Register a new user with valid credentials
    Given I am on the register page
    When I fill in "username" with "user1"
    And I fill in "password" with "password"
    And I fill in "password_confirmation" with "password"
    And I press "Register"
    Then I should see "You have successfully registered"
    And I should see "Logout" in the "navbar"
    And I should see "user1" in the "navbar"