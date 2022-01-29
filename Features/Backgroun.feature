Feature: Testing FB application
  Background: Common Steps
    Given Browser open
    When I Pass the url

  Scenario: Testing the valid credentials
    Then valid credentials

  Scenario: Testing the invalid credentials
    Then I enter the invalid crednetials