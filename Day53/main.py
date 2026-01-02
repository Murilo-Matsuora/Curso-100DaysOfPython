import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(zillow_url)
zillow_html = response.text

soup = BeautifulSoup(zillow_html, "html.parser")

sales_data = []
sale_cards = soup.find_all(class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
for sale_card in sale_cards:
    address = sale_card.find(attrs={'data-test': 'property-card-addr'}).getText().strip().replace(" | ", " ")
    price = sale_card.find(class_="PropertyCardWrapper__StyledPriceLine").getText().replace(" ", "").removesuffix("1bd").removesuffix("/mo").removesuffix("+")
    link = sale_card.find(attrs={'data-test': 'property-card-link'})['href']

    # print(address)
    # print(price)
    # print(link)

    sales_data.append({
        "address": address,
        "price": price,
        "link": link,
    })

# print(sales_data)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

for sale in sales_data:
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf3kVN-BpYWbh4kkJ9VnkJT_i8ji-fHijtqxInMNRsjNnMsDA/viewform?usp=header")

    time.sleep(2)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_forms_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_input.send_keys(sale["address"])
    price_input.send_keys(sale["price"])
    link_input.send_keys(sale["link"])
    send_forms_btn.click()

