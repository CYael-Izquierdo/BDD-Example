Feature: Logging in

  Background:
    Given I am on home page

  @fixture.browser.chrome @Working
  Scenario Outline: Login with a valid account

    When I go to login page
    And I fill username with <username>, password with <password> and press login
    Then I should see logged in as <username>

    Examples: Accounts
    | username      | password  |
    | user          | bitnami1  |
    | testaccount1  | TestPsw1  |

  @fixture.browser.chrome @Working
  Scenario Outline:

    When I go to login page
    And I fill username with <username>, password with <password> and press login
    Then I should see "Invalid user or password" alert

    Examples: Accounts
    | username    | password   |
    | user        | asd1234    |
    | hola        | bitnami1   |