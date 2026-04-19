from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import json
import os

app = Flask(__name__)

line_bot_api = LineBotApi('/QwqfXBku/ElGhmuTmVZQGMKLtvlZ04SQAwiS8W+n0I+q5Z8WDFnpp+l68hVJNRCgOzvc+5TnXd2yCZ/FR7a8wJ/dqCqXRoXGGFIXO1NZDfE+zq+kFpMfsEPcFUReoI95NURX950jsA4zlPhL264RQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('101a98c69f633f562efe030ec346883a')

# データ読み込み
def load_data():
    if os.path.exists("birthdays.json"):
        with open("birthdays.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# データ保存
def save_data(data):
    with open("birthdays.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

birthdays = load_data()

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    signature = request.headers['X-Line-Signature']
    handler.handle(body, signature)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.strip()

    # 👉 「誕生日」で始まる時だけ反応
    if text.startswith("誕生日"):
        try:
            parts = text.split()

            # 形式チェック
            if len(parts) != 3:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="使い方：誕生日 名前 04-15")
                )
                return

            _, name, date = parts

            birthdays[name] = date
            save_data(birthdays)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=f"{name}の誕生日（{date}）を登録したよ！🎉")
            )

        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="エラー：誕生日 名前 04-15 で送ってね")
            )

    # 👉 それ以外は完全無視（重要）
    return

if __name__ == "__main__":
    app.run(port=5000)