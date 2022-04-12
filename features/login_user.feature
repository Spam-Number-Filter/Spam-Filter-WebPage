Feature: login user
  In order to do Create, Read, Update and Delete (CRUD) operations
  As a user
  I want to login to the webpage with some valid credentials

  Background: There is a register user with username "admin" and password "admin"
    Given Exists a user "admin" with password "admin"

  Scenario: login a valid user with valid credentials
    Given I login as user "admin" with password "admin"
    When I click on the login button
    Then I should see the main page
    And I should see the logout button on the top right corner of the navbar

  Scenario: login a valid user with invalid credentials
    Given I login as user "admin" with password "notadmin"
    When I click on the login button
    Then I should see the login page
    And I should see an error message