from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_events = []
upcoming_events_selenium = driver.find_elements(By.CSS_SELECTOR, " .event-widget .menu li")

for upcoming_event in upcoming_events_selenium:
    event_date = upcoming_event.find_element(By.TAG_NAME, "time").text
    event_name = upcoming_event.find_element(By.TAG_NAME, "a").text
    upcoming_events.append({
        "time": event_date,
        "name": event_name,
    })

print(upcoming_events)

driver.quit()








#---------------------------------------------------------------------------------------------------------------------------
# PART 1
#---------------------------------------------------------------------------------------------------------------------------
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com.br/CAIXA-PEBBLE-TIPO-PRETA-51MF1680AA000/dp/B07VVP8BGD/?_encoding=UTF8&pd_rd_w=pENvs&content-id=amzn1.sym.9d4cd3f8-955c-4000-9b8a-43f9dce62737%3Aamzn1.symc.050ea944-f1cf-4610-b462-3b604f2f4082&pf_rd_p=9d4cd3f8-955c-4000-9b8a-43f9dce62737&pf_rd_r=07VYTDW059H49GSN5P1A&pd_rd_wg=D3oHf&pd_rd_r=459be3d5-c0ea-4775-b846-d20b895b7319&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d&th=1")

# continue_buying_btn = driver.find_element(By.CLASS_NAME, "a-button-text")
# continue_buying_btn.click()

# price_currency = driver.find_element(By.CLASS_NAME, "a-price-symbol")
# price_dollars = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_currency.text} {price_dollars.text}.{price_cents.text}")

# add_to_cart_btn = driver.find_element(By.CSS_SELECTOR, value="#a-autoid-21 .a-button-text")
# print(f"{add_to_cart_btn.text}")

# international_purchase_img = driver.find_element(By.XPATH, '//*[@id="availabilityInsideBuyBox_feature_div"]/div/div[3]/img')
# print(f"{international_purchase_img}")

# driver.close()
# driver.quit()