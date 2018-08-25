# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('rRSuvGwreE0/ysfxPIatexqDe/P/vuSoGn+ls8zO649l0qah/GWxcPg4WZiLDim+5puFTI2JJw6I3D2eKADHz0XINJk1/Potg9tZaZ5UGd+11kU7Bwe+rudcYy3xNGRVTg5Y4xDTN2WrpvHBb4YZGgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('de519a7cf5e328fbcb2f9476cbff0df5')



@app.route("/callback", methods=['POST'])
def callback():

    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)