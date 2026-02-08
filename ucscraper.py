from seleniumbase import Driver
import time

#driver = Driver(uc=True, agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

driver = Driver(uc=True, incognito=True)

try:
    url = "https://www.ralphs.com"

    driver.uc_open_with_reconnect(url, reconnect_time=6)

    driver.uc_gui_click_captcha()

    time.sleep(4)

    if "Access Denied" in driver.get_page_source():
        print("Detected, attempt cookie clear and reload")
        driver.delete_all_cookies()
        driver.execute_script("window.location.reload()")
        time.sleep(5)
    print(f"Page Title: {driver.title}")

finally:
    driver.quit()
