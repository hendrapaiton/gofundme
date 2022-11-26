from playwright.sync_api import sync_playwright
from bot.search import Search
import sys


if __name__ == '__main__':
    params = sys.argv[1]
    search = Search()
    
    with sync_playwright() as playwright:
        search.run(playwright, 'https://www.gofundme.com/s?q='+params)
