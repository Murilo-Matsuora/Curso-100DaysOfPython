from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

def signup():
    signup_btn = driver.find_element(By.ID, value="toggle-login-register")
    signup_btn.click()

    driver.implicitly_wait(10)

    with open(file="signup_data.json",mode="r") as file:
        data = json.load(file)
        signup_name = data["chrome_signup"]["name"]
        signup_email = data["chrome_signup"]["email"]
        signup_password = data["chrome_signup"]["password"]

    name_input = driver.find_element(By.ID, value="name-input")
    email_input = driver.find_element(By.ID, value="email-input")
    password_input = driver.find_element(By.ID, value="password-input")

    name_input.send_keys(signup_name)
    email_input.send_keys(signup_email)
    password_input.send_keys(signup_password, Keys.ENTER)
def login_as_admin():
    try:
        with open(file="login_data.json",mode="r") as file:
            data = json.load(file)
            login_email = data["chrome_login"]["email"]
            login_password = data["chrome_login"]["password"]
    except OSError:
        print("No login data found in computer. Reading information from the website instead.")

        all_login_data = driver.find_elements(By.CLASS_NAME, value="Login_credentialGroup__xutMX")

        login_data = all_login_data[1].find_elements(By.CLASS_NAME, value="Login_credentialDetail__Mu9oI")

        login_email = ""
        login_password = ""
        for entry in login_data:
            if "email" in entry.text.lower():
                login_email = entry.text.replace("Email: ", "")
            elif "password" in entry.text.lower():
                login_password = entry.text.replace("Password: ", "")
            else:
                print("Not email or password, ignoring...")

        if login_email == "" or login_password == "":
            print("Couldn't read email or password from website.")
            raise LookupError
    
    email_input = driver.find_element(By.ID, value="email-input")
    password_input = driver.find_element(By.ID, value="password-input")
    email_input.send_keys(login_email)
    password_input.send_keys(login_password, Keys.ENTER)
def advance_three_days():
    advance_three_days_btn = driver.find_element(By.ID, "advance-3-days")
    advance_three_days_btn.click()
def logout():
    logout_btn = driver.find_element(By.ID, "logout-button")
    logout_btn.click()
def enable_simulation():
    enable_simulation_checkbox = driver.find_element(By.ID, value="network-enabled-toggle")
    enable_simulation_checkbox.click()

    driver.implicitly_wait(10)

    failure_rate_slider = driver.find_element(By.ID, "failure-rate-slider")
    failure_rate_slider.click()
    for _ in range(10):
        failure_rate_slider.send_keys(Keys.RIGHT)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

login_btn = driver.find_element(By.ID, value="login-button")
login_btn.click()

driver.implicitly_wait(10)

login_as_admin()
driver.implicitly_wait(10)
advance_three_days()
driver.implicitly_wait(10)
enable_simulation()



    
