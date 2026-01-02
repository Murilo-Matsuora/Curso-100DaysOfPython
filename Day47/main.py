from bs4 import BeautifulSoup
import requests
import smtplib
import json


with open(file="sensitive_data.json", mode='r') as f:
    SENSITIVE_DATA = json.load(f)

AMAZON_URL = "https://www.amazon.com.br/HP-Speaker-DHS-2111S-Alimentacao-conector/dp/B09MC7ZK7M/ref=sr_1_15?crid=9PL3HOS32VO1&dib=eyJ2IjoiMSJ9.8M6setNZCkk5khDHC1ghOJmPUkI4yx3QxtCJDeq5VYP4a4P8sIVhuMHshvV15H2A5ANvcbB8DwC3ihQpb2ZmyNbf0l3rrgFgzVM8pLg2EZDF4Ylihvv-o6bTp1v_NVOl-Z4nNblKDFAjxOhKm64jLBBbhlhLbPTrEYOszxCE-vb5N9VAlfkaSJhIPvkY76b7bFGkfzBUISAyZMBXAgi92MgNP8iATadmopfuy3bn6VM2sd6DqQ2hyvuXtWgSaeMgergAJYeJa263M6BRL7eY4XeTqXwfmF92_fBZyYIiJtw.fNbe_SAeSg9z7cNp1hSgATvNAbijMBIJ5k2FsM9hDJE&dib_tag=se&keywords=caixa+de+som+para+pc&qid=1766790798&sprefix=caixa+de+som+%2Caps%2C195&sr=8-15&ufe=app_do%3Aamzn1.fos.db68964d-7c0e-4bb2-a95c-e5cb9e32eb12"
URL_HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0",
}
SENDER_EMAIL = SENSITIVE_DATA["smtp_sender"]["email"]
SENDER_PASSWORD = SENSITIVE_DATA["smtp_sender"]["password"]
RECEIVER_ADDRESS = SENSITIVE_DATA["smtp_receiver"]["email"]
PRICE_LIMIT_ALERT = 120.00


response = requests.get(url=AMAZON_URL, headers=URL_HEADER)
amazon_html = response.text

soup = BeautifulSoup(amazon_html, "html.parser")

product_name = soup.find(name="span", id="productTitle").getText()
price_symbol = soup.find(name="span", class_="a-price-symbol").getText()
price_punctiation = soup.find(name="span", class_="a-price-decimal").getText()
price_whole = soup.find(name="span", class_="a-price-whole").getText()[:-1]
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()

price_text = f"{price_symbol} {price_whole}{price_punctiation}{price_fraction}"
price_float = float(f"{price_whole}.{price_fraction}")

print(price_float)

if price_float < PRICE_LIMIT_ALERT:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECEIVER_ADDRESS,
            msg=(f"Subject:Preço baixo em {product_name}\n\nEle está custando {price_text} em {AMAZON_URL}.").encode('utf-8')
        )
