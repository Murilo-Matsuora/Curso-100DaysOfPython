from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_element = driver.find_element(By.NAME, "fName")
last_name_element = driver.find_element(By.NAME, "lName")
email_element = driver.find_element(By.NAME, "email")

first_name_element.send_keys("Abcdef")
last_name_element.send_keys("Ghijkl")
email_element.send_keys("Mnopqrs@mail.com", Keys.ENTER)

