STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from API import creds
from twilio.rest import Client
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use "https://www.alphavantage.co/query"
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price.

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.

parameters_for_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": creds.ALPHAVANTAGE_API_KEY
}
response_stock_news = requests.get(STOCK_ENDPOINT,params=parameters_for_stock)
response_stock_news.raise_for_status()
stock_news = response_stock_news.json()

trading_days = list(stock_news['Time Series (Daily)'].keys())
yesterday = trading_days[0]
day_before_yesterday = trading_days[1]
closing_price_yesterday = float(stock_news['Time Series (Daily)'][yesterday]['4. close'])
closing_price_day_before_yesterday = float(stock_news['Time Series (Daily)'][day_before_yesterday]['4. close'])
print(closing_price_yesterday,closing_price_day_before_yesterday)

upDown = ""
if (closing_price_yesterday - closing_price_day_before_yesterday) > 0:
    upDown = "🔺"
else:
    upDown = "🔻"

percentage_change = abs((closing_price_yesterday - closing_price_day_before_yesterday) / closing_price_day_before_yesterday * 100)
if percentage_change >= 5:
    #this is news data
    parameters_for_news = {
        "qInTitle": COMPANY_NAME,
        "apiKey": creds.NEWS_API_KEY
    }
    response_news = requests.get(NEWS_ENDPOINT, parameters_for_news)
    response_news.raise_for_status()
    news_data = response_news.json()["articles"][:3]
    formatted_news = [f"{STOCK}: {upDown}{round(percentage_change)}%"
                       f"\nHeadLine: {article['title']}." for article in news_data]

    account_sid = creds.account_sid
    auth_token = creds.auth_token
    client = Client(account_sid, auth_token)
    for article in formatted_news:
        message = client.messages.create(
            body=article,
            from_="+18125613420",
            to="+919666225131",
        )
        print(message.sid)
        print(message.status)
else:
    print("No news")





#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are 
required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st,
near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required 
to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, 
near the height of the coronavirus market crash.
"""

