Feature: Logging in

  Background:
    Given a web browser is at the redmine login page

  @fixture.browser.chrome @Working
  Scenario Outline: Login with a valid account

    When I fill username with <username>, password with <password> and press login
    Then I should see logged in as <username>

    Examples: Accounts
    | username      | password  |
    | user          | bitnami11  |
    | testaccount1  | TestPsw1 |

  @fixture.browser.chrome @Working
  Scenario Outline:

    When I fill username with <username>, password with <password> and press login
    Then I should see "Invalid user or password" alert

    Examples: Accounts
    | username    | password   |
    | user        | asd1234    |
    | hola        | bitnami1   |