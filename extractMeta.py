from collections import defaultdict
import sys
import atexit
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

class LeetCodeClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = "https://leetcode.com"
        self.login_url = "https://leetcode.com/accounts/login/"
        self.profile_url = f"https://leetcode.com/u/{username}/"  # Ensure correct profile URL

    def selenium_login(self):
        """Use undetected Selenium to log into LeetCode and fetch pages."""
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")  # Stealth mode
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--mute-audio")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")
        options.add_argument("--disable-popup-blocking")

        driver = uc.Chrome(options=options)

        atexit.register(self.quit_driver)  # Ensure the driver quits on exit

        driver.get(self.login_url)

        try:
            # Wait until login fields are visible
            wait = WebDriverWait(driver, 15)
            username_input = wait.until(EC.presence_of_element_located((By.NAME, "login")))
            password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

            # Enter credentials
            username_input.send_keys(self.username)
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.RETURN)

            time.sleep(10)  # Allow Cloudflare to process

            print("✅ Login successful via Selenium.")
            return driver  # Return the driver for fetching pages

        except Exception as e:
            print(f"❌ Error during login: {e}")
            driver.quit()
            return None

    def fetch_page_with_selenium(self, driver, url):
        """Use Selenium to fetch pages that Cloudflare blocks."""
        try:
            driver.get(url)
            time.sleep(7)  # Allow Cloudflare to process
            page_source = driver.page_source
            print(f"✅ Successfully fetched {url}")
            return page_source
        except Exception as e:
            print(f"❌ Failed to fetch {url}: {e}")
            return None
        
    def quit_driver(self):
        """Properly close the driver to avoid WinError 6."""
        if self.driver:
            try:
                self.driver.quit()
                print("✅ Selenium driver closed successfully.")
            except OSError:
                print("⚠️ Driver was already closed. Skipping quit.")
            except Exception as e:
                print(f"⚠️ Unexpected error while closing driver: {e}")
            finally:
                self.driver = None  # Ensure reference is removed

if __name__ == "__main__":
    username = "Mavrikx"
    password = "Vader1994!"

    leetcode = LeetCodeClient(username, password)
    driver = leetcode.selenium_login()
    if driver:
        full_list = defaultdict(int)

        '''
        thirty_days = leetcode.fetch_page_with_selenium(driver, "https://leetcode.com/company/facebook/?favoriteSlug=facebook-thirty-days")

        time.sleep(10)

        soup = BeautifulSoup(thirty_days, 'html5lib')

        table = soup.find_all('div', attrs = {'class':'ellipsis line-clamp-1'}) 

        for row in table[:150]:
            full_list[row.text] += 1

        '''


        # ---------------------------------------------------------------------

        three_months = leetcode.fetch_page_with_selenium(driver, "https://leetcode.com/company/facebook/?favoriteSlug=facebook-three-months")

        time.sleep(10)

        soup = BeautifulSoup(three_months, 'html5lib')

        table = soup.find_all('div', attrs = {'class':'ellipsis line-clamp-1'}) 

        for row in table[:150]:
            full_list[row.text] += 1

        # ---------------------------------------------------------------------

        six_months = leetcode.fetch_page_with_selenium(driver, "https://leetcode.com/company/facebook/?favoriteSlug=facebook-six-months")

        time.sleep(5)

        soup = BeautifulSoup(six_months, 'html5lib')

        table = soup.find_all('div', attrs = {'class':'ellipsis line-clamp-1'}) 

        for row in table[:150]:
            full_list[row.text] += 1

        print({k: v for k, v in sorted(full_list.items(), key=lambda item: item[1], reverse=True)})

        time.sleep(5)
        
        # Manually close the driver to prevent WinError 6
        leetcode.quit_driver()
        sys.exit()