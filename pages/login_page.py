from playwright.sync_api import Page


class LoginPage:
    URL = "https://automationexercise.com/login"

    def __init__(self, page: Page):
        # Keep the browser tab so every method can use it
        self.page = page
        # data-qa picks the LOGIN form fields, not the signup form's email box
        self.email_input = page.locator("[data-qa='login-email']")
        self.password_input = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")

    def open(self):
        # Go to the login page; goto waits until the page has loaded
        self.page.goto(self.URL)

    def login(self, email, password):
        # Fill the form and submit it; Playwright waits for each element automatically
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
