from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp

sb = sb_cdp.Chrome(locale="en")
endpoint_url = sb.get_endpoint_url()

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(endpoint_url)
    context = browser.contexts[0]
    page = context.pages[0]
#    query = "Chocolate"
#    url = f"https://www.ralphs.com/search?query={query}&searchType=default_search"
    url = "https://www.ralphs.com"
    page.goto(url, wait_until="networkidle")
    sb.sleep(3000)
    sb.solve_captcha()
    sb.sleep(3)
    content = page.content()
print(content)
