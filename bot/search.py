from playwright.sync_api import Playwright
import time


class Search:
    def run(self, playwright: Playwright, url: str):
        browser = playwright.chromium.launch(headless=True, slow_mo=1000)
        context = browser.new_context()

        page = context.new_page()
        page.goto(url)
        page.set_default_timeout(5000)

        def infinity():
            try:
                before = len(page.query_selector_all(
                    '//ul[@id="search-list"]/li/a')
                )
                page.get_by_text('Show More').click()
                time.sleep(2)
                after = len(page.query_selector_all(
                    '//ul[@id="search-list"]/li/a')
                )
                print(before, after)
                if before < after:
                    return infinity()
            except:
                context.close()
                browser.close()

        if page.get_by_text('Show More').is_visible():
            infinity()

        context.close()
        browser.close()
