import requests

from twilio.rest import Client

STOCK = "RELIANCE.BSE"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "MYCWLUH9HJDYOLUY"
twilio_account_sid = 'AC852fce9ecaa14fedfbcc4cb026ede1a8'
twilio_auth_token = 'c35ad987ab5e655f514824b895781c48'
parameters = {
    'function': 'TIME_SERIES_DAILY',
    "symbol": STOCK,
    "apikey": "MYCWLUH9HJDYOLUY"

}

news_params = {
    "qInTitle": "reliance",
    "apiKey": "7490be26890a4f669644fd1678962387",
    "sortBy": "popularity"
}
response = requests.get("https://www.alphavantage.co/query", params=parameters)
data = response.json()
stock_data = data["Time Series (Daily)"]
data_list = []
for i in stock_data:
    val = stock_data[i]
    data_list.append(val)
print(data_list)
yesterday_closing_price = float(data_list[1]["4. close"])
dby_closing_price = float(data_list[2]["4. close"])
diff = yesterday_closing_price - dby_closing_price
change_percent = ((diff / dby_closing_price) * 100).__round__(2)
if change_percent>0:
    emoji="⬆️"
else:
    emoji="🔻    "
if change_percent >= 1 or change_percent <= -1:
    response_news = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_data = response_news.json()
    news_list = []
    for i in range(0, 3):
        headline = (news_data["articles"][i]["title"])
        news_list.append(headline)
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
        body=f" BluPython STOCK PRICE ALERT Company : Reliance Price Change{emoji} {change_percent}% Business News "
             f"HighLights: {news_list[0]}||{news_list[1]}||{news_list[2]} ",
        from_='+15078795338',
        to='+919742757917'
    )
