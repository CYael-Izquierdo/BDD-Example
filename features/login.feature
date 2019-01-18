Feature: Logging in

  @fixture.browser.chrome @Working @tl.remine.tp1
  Scenario Outline: Login with a valid account

    Given a web browser is at the redmine login page
    When I fill username with <username>, password with <password> and press login
    Then I should see logged in as <username>

    Examples: Accounts
      | username     | password |
      | user         | bitnami1 |

  @fixture.browser.chrome @Working @tl.remine.tp1
  Scenario Outline: Login with a <scenario> account

    Given a web browser is at the redmine login page
    When I fill username with <username>, password with <password> and press login
    Then I should see "Invalid user or password" alert

    Examples:
      | scenario            | username | password |
      | invalid username    | user     | asd1234  |
      | invalid password    | hola     | bitnami1 |