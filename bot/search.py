from playwright.sync_api import Playwright


class Search:
    def run(self, playwright: Playwright, url: str):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto(url)

        context.close()
        browser.close()



