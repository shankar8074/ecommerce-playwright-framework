import os

import pytest
# Page is the browser tab type; expect gives assertions that retry automatically
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import LoginPage


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

    # Create the page objects, both sharing the same browser tab
    login_page = LoginPage(page)
    home_page = HomePage(page)

    # Open the login page and sign in
    login_page.open()
    login_page.login(email, password)

    #Check the header shows the logged-in user; expect keeps retrying for up to 5 seconds
    expect(home_page.logged_in_as_text).to_be_visible()
    expect(home_page.logged_in_as_text).to_contain_text("Logged in as shankar")
