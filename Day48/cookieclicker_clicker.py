from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def buy_most_expernsive_purchase():
    available_products = driver.find_elements(By.CSS_SELECTOR, '#products [class="product unlocked enabled"]')
    prices = []
    for product in available_products:
        price  = product.find_element(By.CLASS_NAME, "price")
        prices.append(float(price.text))
    print(prices)
    largest_price = max(prices)
    most_expensive_product_index = prices.index(largest_price)
    most_expensive_product = available_products[most_expensive_product_index]
    most_expensive_product.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker")

time.sleep(1)

english_btn = driver.find_element(By.ID, "langSelect-EN")
english_btn.click()
time.sleep(1)

cookie_btn = driver.find_element(By.ID, "bigCookie")

start_time = time.time()
end_time = start_time + 5*60

while time.time() < end_time:
    five_sec_later = time.time() + 5
    while time.time() < five_sec_later:
        cookie_btn.click()
    print("5 sec later")
    buy_most_expernsive_purchase()


