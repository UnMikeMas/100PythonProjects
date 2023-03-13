import requests
import smtplib
import datetime


def get_news(COMPANY_NAME, NEWS_ENDPOINT):
    NEWS_API_KEY = "api_key"
    NEWS_PARAMETERS = {
        "q": COMPANY_NAME,
        "from": datetime.datetime.now(),
        "sortby": "popularity", 
        "apiKey": NEWS_API_KEY,
    }

    news_request = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_data = news_request.json()
    list = []
    for i in range(0,3):
        list.append(news_data["articles"][i]["title"])
        mail_sender(COMPANY_NAME, list)
        
        
def stock_prices():
    STOCK_NAME = "TSLA"
    COMPANY_NAME = "Tesla Inc"

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    STOCK_API_KEY = "api_key"
    STOCK_PARAMETERS = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": STOCK_NAME,
        "interval": "60min",
        "apikey": STOCK_API_KEY,
    }

    stock_request = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
    stock_data = stock_request.json()
    open_data = float(stock_data["Time Series (60min)"]["2023-02-16 20:00:00"]["1. open"])
    close_data = float(stock_data["Time Series (60min)"]["2023-02-17 20:00:00"]["4. close"])

    if not open_data*0.95 <= close_data <= 1.05*open_data:
        get_news(COMPANY_NAME, NEWS_ENDPOINT)


def mail_sender(COMPANY_NAME, list):
    PARAGRAPH = "\n".join(list)
    MY_EMAIL = "mymail"
    PASSWORD = "mypassword"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="to_mail",
            msg=f"Stock price change in {COMPANY_NAME}\n\nThere has been a price change in {COMPANY_NAME}, here are some headlines: {PARAGRAPH}"
        )

stock_prices()
