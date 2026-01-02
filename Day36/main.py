import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = ""
with open(file="alphavantage_api.txt",mode='r') as f:
    STOCK_API = f.read()

NEWS_API = ""
with open(file="news_api.txt",mode='r') as f:
    NEWS_API = f.read()

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API,
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

data = response.json()['Time Series (Daily)']

yesterday_closing = float(list(data.values())[1]['4. close'])
day_before_yesterday_closing = float(list(data.values())[2]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

pos_diff = abs(yesterday_closing - day_before_yesterday_closing)

print(pos_diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_diff = (pos_diff / yesterday_closing)

print(percentage_diff)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if percentage_diff < 5:
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()

    data = response.json()
    # print(data)
    # print(data.keys())

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    all_articles = data['articles']

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = all_articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
    


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 

    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    for article in three_articles:
        message = client.messages.create(
            messaging_service_sid='MG016966014a8687880aea2dd8df0b2fb3',
            body=f'{article['title']}\n{article['description']}',
            to='+5511995958918'
        )
        print(message.status)

        for (key, value) in article.items():
            print(f"{key}:")
            print(value)
            
        print("\n\n")


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

