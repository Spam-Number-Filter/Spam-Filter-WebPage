Feature: Register User
  In order to have an account on the website
  As a user
  I want to create and register a user with the credentials of my choice

  Background: There is a registered user
    Given Exists a user with username "user", password "password" and email "email@sample.com"

  Scenario: Register a new user with already taken username
    Given I am on the register page
    When I enter my credentials
      | username | first_name | last_name | email            | password1    | password2             |
      | user     | John       | Doe       | user@sample.com  | usersecret1  | usersecret1           |
    And I press "Register"
    Then I should see an error message

  Scenario: Register a new user with already taken email
    Given I am on the register page
    When I enter my credentials
      | username | first_name | last_name | email            | password1    | password2             |
      | newuser  | John       | Doe       | email@sample.com | usersecret1  | usersecret1           |
    And I press "Register"
    Then I should see an error message

  Scenario: Register a new user failing password confirmation
    Given I am on the register page
    When I enter my credentials
      | username | first_name | last_name | email            | password1    | password2             |
      | newuser  | John       | Doe       | user@sample.com  | usersecret1  | wrongpass             |
    And I press "Register"
    Then I should see an error message

  Scenario: Register a new user with an invalid password
    Given I am on the register page
    When I enter my credentials
      | username | first_name | last_name | email            | password1    | password2             |
      | newuser  | John       | Doe       | user@sample.com  | pass         | pass                  |
    And I press "Register"
    Then I should see an error message

  Scenario: Register a new user with an invalid username
    Given I am on the register page
    When I enter my credentials
      | username | first_name | last_name | email            | password1    | password2             |
      | ¬~@user  | John       | Doe       | user@sample.com  | usersecret1  | usersecret1           |
    And I press "Register"
    Then I should see an error message

  Scenario: Register a new user with an invalid first name
    Given I am on the register page
    When I enter my credentials
      | username | first_name | last_name | email            | password1    | password2             |
      | newuser  | ¬~@John    | Doe       | user@sample.com  | usersecret1  | usersecret1           |
    And I press "Register"
    Then I should see an error message

  Scenario: Register a new user with an invalid last name
    Given I am on the register page
    When I enter my credentials
      | username | first_name | last_name | email            | password1    | password2             |
      | newuser  | John       | ¬~@Doe    | user@sample.com  | usersecret1  | usersecret1           |
    And I press "Register"
    Then I should see an error message

  Scenario: Register a new user with valid credentials
    Given I am on the register page
    When I enter my credentials
      | username | first_name | last_name | email            | password1    | password2             |
      | newuser  | John       | Doe       | user@sample.com  | usersecret1  | usersecret1           |
    And I press "Register"
    Then I should see I am logged in