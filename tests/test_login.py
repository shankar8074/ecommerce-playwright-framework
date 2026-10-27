import os

import pytest
# Page is the browser tab type; expect gives assertions that retry automatically
from playwright.sync_api import Page, expect


# Credentials come from environment variables so they are never saved in the code
# (or in git), and each person or CI server can use its own account
def get_env(name):
    # Read the variable; stop the test with a clear message if it is not set
    value = os.environ.get(name)
    if not value:
        pytest.fail(f"Environment variable {name} is not set. Please set it before running the tests.")
    return value


# pytest-playwright passes in a fresh "page" (browser tab) for each test
def test_login_with_valid_credentials(page: Page):
    # Read the login details from the environment
    email = get_env("TEST_USER_EMAIL")
    password = get_env("TEST_USER_PASSWORD")

    # Open the login page; goto waits until the page has loaded
    page.goto("https://automationexercise.com/login")

    # Type the email into the LOGIN form's email box (data-qa avoids the signup email box)
    page.locator("[data-qa='login-email']").fill(email)

    # Type the password into the login form's password box
    page.locator("[data-qa='login-password']").fill(password)

    # Click Login; Playwright waits for the button to be visible and enabled first
    page.locator("[data-qa='login-button']").click()

    # Check the header shows the logged-in user; keeps retrying for up to 5 seconds
    expect(page.get_by_text("Logged in as Shankar")).to_be_visible()
