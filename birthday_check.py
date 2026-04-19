import json
import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage

line_bot_api = LineBotApi('/QwqfXBku/ElGhmuTmVZQGMKLtvlZ04SQAwiS8W+n0I+q5Z8WDFnpp+l68hVJNRCgOzvc+5TnXd2yCZ/FR7a8wJ/dqCqXRoXGGFIXO1NZDfE+zq+kFpMfsEPcFUReoI95NURX950jsA4zlPhL264RQdB04t89/1O/w1cDnyilFU=')

with open("birthdays.json", "r", encoding="utf-8") as f:
    birthdays = json.load(f)

today = datetime.datetime.now().strftime("%m-%d")

for name, date in birthdays.items():
    if date == today:
        line_bot_api.push_message(
            "C586325c27c73b029184f728605c36057",
            TextSendMessage(text=f"{name}さん誕生日おめでとう🎂")
        )