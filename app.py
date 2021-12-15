import random
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, FlexSendMessage, 
    TemplateSendMessage, ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction,
    ButtonsTemplate, URITemplateAction, TextSendMessage
)

app = Flask(__name__)

ACCESS_TOKEN = 'KlTXiq+PhZwdtrmanTbE7SXwtmmY1EfM+aJzuORy7gcqwPfZyLl4jPiVg/dwlY56YuLfQL4BZZgR8lzdFB0I+Ttbm8ZUWaZP9B9TJSnYgRxgXkYKRnKfzDJBhhQ//rrMYu1y9AUx5rDjR4SXUVrvrQdB04t89/1O/w1cDnyilFU='
SECRET = 'bb513754344a36ad5cd59a9ccb1c104b'

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    t = {'Kalau kamu bisa jadi tidak terlihat, apa hal pertama yang akan kamu lakukan?':1, 
        'Apa rahasia yang kamu sembunyikan dari orangtuamu?':2,
        'Siapa orang yang diam-diam kamu sukai?' :3,
        'Siapa orang terakhir yang kamu kepoin di media sosial?':4,
        'Kalau ada jin yang memberikanmu tiga permohonan, apa yang kamu inginkan?':5,
        'Jika kamu kembali ke masa lalu, apa yang akan kamu lakukan?':6,
        'Apa tontonan favoritmu saat masih kecil?': 7,
        'Siapa orang yang paling sering kamu chat?':8,
        'Apa kebohongan terbesar yang pernah kamu katakan kepada orangtuamu?':9,
        'Apa mimpi paling aneh yang pernah kamu alami?':10,
        'Ceritakan detail ciuman pertamamu…':11,
        'Kapan terakhir kali kamu ngompol atau eek di celana?':12,
        'Menurutmu, hewan apa yang terlihat paling mirip denganmu?':13,
        'Di antara temanmu, siapa orang yang paling kamu suka dalam konteks romantis?':15,
        'Di antara temanmu, siapa orang yang menurutmu paling baik dan paling buruk sifatnya?':16,
        'Siapa mantan terindahmu?':16,
        'Siapa orang yang ingin kamu jadikan istri/suami?':17,
        'Apakah kamu pernah melakukan ghosting?':18,
        'Apa aib yang kamu sembunyikan dari teman-temanmu?':19,
        'Berapa jumlah mantanmu? sebutkan!':20,
        }
    tth = random.choice(list(t.keys()))
    pesan = TextSendMessage(tth + "\n" + "Apakah bisa melakukan tantangan ini? Ketik 'bisa' jika memang bisa dan ketik 'gabisa' jika tidak mampu melakukannya"), line_bot_api.reply_message(event.reply_token, tth)

    if msg_from_user == 'Tes':
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.pinimg.com/564x/0d/b8/98/0db89880dfa0595585f33ddb50da89f9.jpg',
                title='Menu',
                text='Please select',
                actions=[
                    URITemplateAction(
                        label='uri',
                        uri= 'pesan'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
