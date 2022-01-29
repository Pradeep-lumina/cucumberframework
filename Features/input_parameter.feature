Feature: Facebook application

  Scenario: Valid credentials
    Given Open the browser
    When Enter the url
    Then Enter the username "test" and password "test123"
    And Close the browser


  Scenario Outline: Valid credentials
    Given Open the browser
    When Enter the url
    Then Enter the username "<username>" and password "<password>"
    And Close the browser

    Examples:
      |username  |password|
      |test1     |test2   |
      |test3     |test4   |
      |test5     |test6   |
