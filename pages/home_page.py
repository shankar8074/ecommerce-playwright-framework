from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        # Keep the browser tab so every method can use it
        self.page = page
        # Header link that reads "Logged in as <name>" after a successful login
        self.logged_in_as_text = page.get_by_text("Logged in as")
