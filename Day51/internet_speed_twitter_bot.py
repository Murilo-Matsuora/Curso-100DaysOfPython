import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWNLOAD_SPEED = 150
PROMISED_UPLOAD_SPEED = 50

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)

        self.internet_speed_driver = webdriver.Chrome(options=chrome_options)
        self.x_driver = webdriver.Chrome(options=chrome_options)

        self.download_speed = 0
        self.upload_speed = 0

        with open(file="sensitive_data.json") as f:
            self.x_login_data = json.load(f)["x"]
    
    def run_speed_test(self):
        self.internet_speed_driver.get("https://www.speedtest.net/")
        run_speedtest_btn = self.internet_speed_driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        run_speedtest_btn.click()

        time.sleep(2)
        result = self.internet_speed_driver.find_element(By.CLASS_NAME, "result-label")
        wait = WebDriverWait(self.internet_speed_driver, timeout=180)
        wait.until(lambda _ : result.is_displayed())

        print("Acabou.")

        time.sleep(2)

        self.download_speed = self.internet_speed_driver.find_element(By.CSS_SELECTOR, '[class="result-data-large number result-data-value download-speed"]').text
        self.upload_speed = self.internet_speed_driver.find_element(By.CSS_SELECTOR, '[class="result-data-large number result-data-value upload-speed"]').text

        print(self.download_speed)
        print(self.upload_speed)
    
    def tweet_at_provider(self):
        if self.download_speed < PROMISED_DOWNLOAD_SPEED or self.upload_speed < PROMISED_UPLOAD_SPEED:
            print("Internet speed below the promised. Starting twitting procces...")
            self.x_driver.get("https://x.com/")

            self.x_driver.implicitly_wait(10)            
            login_btn = self.x_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
            login_btn.click()
            
            self.x_driver.implicitly_wait(10)            
            email_input = self.x_driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
            email_input.send_keys(self.x_login_data["email"], Keys.ENTER)

            self.x_driver.implicitly_wait(10)            
            password_input = self.x_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
            password_input.send_keys(self.x_login_data["password"], Keys.ENTER)

