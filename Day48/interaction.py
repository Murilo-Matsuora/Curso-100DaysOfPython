from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[2]/div[1]/div/div[3]/ul/li[2]/a[1]')
print(article_count_element.text)

# Find element by link text
all_portals = driver.find_element(By.LINK_TEXT,"Content portals")
# all_portals.click()

# Find the Search <input> by name
search_icon = driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]')
search_icon.click()
search_bar = driver.find_element(By.NAME, value="search")

# Sending keyboard input through Selenium
search_bar.send_keys("Python",Keys.ENTER)

driver.quit()