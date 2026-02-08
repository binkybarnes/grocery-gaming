from playwright.sync_api import sync_playwright
import time

def scrape_target(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
              user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
              )
        page = context.new_page()

        print(f"Searching Target for {query}...")
        url = f"https://www.target.com/s?searchTerm={query}&category=0%7CAll%7Cmatchallpartial%7Call+categories&searchTermRaw="

        page.goto(url, wait_until="networkidle")
        content = page.content()

def scrape_trader_joes(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
              user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
              )
        page = context.new_page()

        print(f"Searching Trader Joe's for {query}...")
        url = f"https://www.traderjoes.com/home/search?q={query}&global=yes"

        page.goto(url, wait_until="networkidle")
        content = page.content()


def scrape_hmart(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
              user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
              )
        page = context.new_page()

        print(f"Searching HMart for {query}...")
        url = f"https://www.hmart.com/{query}?_q={query}&map=ft"

        page.goto(url, wait_until="networkidle")
        content = page.content()


def scrape_99ranch(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
              user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
              )
        page = context.new_page()

        print(f"Searching 99Ranch for {query}...")
        url = f"https://www.99ranch.com/search?keyword={query}"

        page.goto(url, wait_until="networkidle")
        content = page.content()

    print(content)

def main():
    print("hello")
#    scrape_target("beef")
#    scrape_trader_joes("beef")
#    scrape_hmart("potato")
    scrape_99ranch("potato")
    print("end of script")
    

main()

