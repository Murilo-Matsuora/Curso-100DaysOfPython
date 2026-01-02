import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SIMILAR_ACCOUNT = "canalbrushrush"

def try_login(retries=3, delay=20):
    for attempt in range(retries):
        print(f"Attempt to log in {attempt + 1} of {retries}")
        email_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")

        time.sleep(0.5)
        email_input.clear()
        email_input.send_keys(instagram_data["email"])
        time.sleep(0.5)
        password_input.clear()
        password_input.send_keys(instagram_data["password"])
        time.sleep(1.5)
        login_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        login_btn.click()
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Search"]'))
            )
            print("Login successful")
            return
        except:
            print(f"Login attempt {attempt + 1} failed. Retrying...")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com")
driver.implicitly_wait(10)

with open(file="sensitive_data.json") as file:
    instagram_data = json.load(file)["instagram"]

try_login()

driver.implicitly_wait(10)

# not_now_button = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Lx"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div')
# not_now_button.click()

time.sleep(1.5)
search_btn = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search"]')
search_btn.click()
time.sleep(1)
search_bar = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search input"]')
search_bar.send_keys(SIMILAR_ACCOUNT)

account_link = driver.find_element(By.CSS_SELECTOR, f'a[href="/{SIMILAR_ACCOUNT}/"]')
account_link.click()

driver.implicitly_wait(10)
time.sleep(1)

account_followers = driver.find_element(By.CSS_SELECTOR, f'a[href="/{SIMILAR_ACCOUNT}/followers/"]')
account_followers.click()

driver.implicitly_wait(10)
time.sleep(1)

while True:
    try:
        follow_btn = driver.find_element(By.CSS_SELECTOR, '[class=" _aswp _aswr _aswu _asw_ _asx2"]')
        follow_btn.click()
        time.sleep(2)
    except:
        print("Follow button was not found. Scrolling...")
        found = False
        while not found:
            scroll_box = driver.find_element(By.CSS_SELECTOR, '[class="x6nl9eh x1a5l9x9 x7vuprf x1mg3h75 x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6"]')
            driver.execute_script("arguments[0].scrollBy(0, 500);", scroll_box)
            
            time.sleep(1.5)
            
            new_buttons = driver.find_elements(By.CSS_SELECTOR, '[class=" _aswp _aswr _aswu _asw_ _asx2"]')
            if len(new_buttons) > 0:
                found = True
            else:
                print(f"Button still not found, scrolling again.")
