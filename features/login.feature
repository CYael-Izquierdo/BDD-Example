Feature: Logging in

  @fixture.browser.chrome @Working @testplan-5
  Scenario Outline: Login with a valid account

    Given a web browser is at the redmine login page
    When I fill username with <username>, password with <password> and press login
    Then I should see logged in as <username>

    Examples: Accounts
    | username      | password  |
    | user          | bitnami1  |
    | testaccount1  | TestPsw1  |

  @fixture.browser.chrome @Working
  Scenario Outline:

    Given a web browser is at the redmine login page
    When I fill username with <username>, password with <password> and press login
    Then I should see "Invalid user or password" alert

    Examples: Accounts
    | username    | password   |
    | user        | asd1234    |
    | hola        | bitnami1   |