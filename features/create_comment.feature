Feature: Create a comment on a post
  In order to comment a post
  As a user
  I want to create a comment in a post

  Background: There is a registered user
    Given Exists a user "user2" with password "password2"
    Given Exists a post with post_id "1"
    And I log in as "user2" with password "password2"
    And I am on the post "1" page

  Scenario: Create comment
    When I click on the comment
    And I write a comment
    And i press "Submit"
    Then I should see the comment
