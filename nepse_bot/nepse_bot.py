import requests

channel_id = '@deicide_404'
bot_token = '7714992390:AAFEgHfwGb3fjM5jg3nlnW6iRMkimBgvRRo'

import requests
import json
import time




# fetch data from the API
response = requests.get("https://www.onlinekhabar.com/smtm/home/trending")

# parse into json
data = response.json()

response_data = data["response"]


for item in response_data:
        result = (
        f"Ticker: {item['ticker']}\n"
        f"Ticker Name: {item['ticker_name']}\n"
        f"Latest Price: {item['latest_price']}\n"
        f"Points Change: {item['points_change']}\n"
        f"Percentage Change: {item['percentage_change']}\n"
        f"Traded of Market Cap: {item['traded_of_mkt_cap']}\n"
        "------------------------------------------------------------------\n"
        )
    
        tele_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        payload = {
            
            'chat_id' : channel_id,
            'text' : result,
            'parse_mode' : 'HTML'
        }

        r = requests.post(tele_url, data=payload)
        time.sleep(2)
        