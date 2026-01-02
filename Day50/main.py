import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com")
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10)
original_window = driver.current_window_handle
assert len(driver.window_handles) == 1

driver.fullscreen_window()
driver.implicitly_wait(10)

time.sleep(1)
decline_tems_btn = driver.find_element(By.XPATH, '//*[@id="c1649373191"]/div/div[2]/div/div/div[1]/div[2]/button')
decline_tems_btn.click()
time.sleep(1)
login_btn = driver.find_element(By.XPATH, '//*[@id="c1649373191"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/header/div/div[2]/div[2]/a')
login_btn.click()

driver.implicitly_wait(10)
time.sleep(3)
google_login_btn = driver.find_element(By.XPATH, '//*[@id="c-1563759946"]/div')
google_login_btn.click()

driver.implicitly_wait(10)
wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

time.sleep(3)
with open(file="sensitive_data.json") as f:
    sensitive_data = json.load(f)

email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys(sensitive_data["email"], Keys.ENTER)

# next_btn = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[3]')
# next_btn.click()