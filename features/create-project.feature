Feature: Create new project

  @fixture.browser.chrome @Working
  Scenario: Create new project without modules

    Given I am on home page
    And I am logged in
    When I go to create new project
    And I enter the new project data without modules
    Then I should see a successful creation alert
    And I should be able to find the created project in Projects tab