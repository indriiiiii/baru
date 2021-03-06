import random
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage,  
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    TextSendMessage, ImageSendMessage, StickerSendMessage,
)
app = Flask(__name__)
ACCESS_TOKEN = '4K6XfwLNonuOPGap35wQ6K2ZCtQIWRpbOSxSoGk6UxXjjK6FgWQvXYkvEUM+6mKONxwldrX43hEdu+rldw8PXybhqRMI1DAx8oXmHn4PMRTIYqzaqsnnwe8vaJ0njYSz350KYwO0h2aFobH8BXZdtgdB04t89/1O/w1cDnyilFU='
SECRET = 'f16e76754a971c5d3f4601171a1db943'
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

t = ['Kalau kamu bisa jadi tidak terlihat, apa hal pertama yang akan kamu lakukan?', 
        'Apa rahasia yang kamu sembunyikan dari orangtuamu?',
        'Siapa orang yang diam-diam kamu sukai?',
        'Siapa orang terakhir yang kamu kepoin di media sosial?',
        'Kalau ada jin yang memberikanmu tiga permohonan, apa yang kamu inginkan?',
        'Jika kamu kembali ke masa lalu, apa yang akan kamu lakukan?',
        'Apa tontonan favoritmu saat masih kecil?',
        'Siapa orang yang paling sering kamu chat?',
        'Apa kebohongan terbesar yang pernah kamu katakan kepada orangtuamu?',
        'Apa mimpi paling aneh yang pernah kamu alami?',
        'Ceritakan detail ciuman pertamamuâ€¦',
        'Kapan terakhir kali kamu ngompol atau eek di celana?',
        'Menurutmu, hewan apa yang terlihat paling mirip denganmu?',
        'Di antara temanmu, siapa orang yang paling kamu suka dalam konteks romantis?',
        'Di antara temanmu, siapa orang yang menurutmu paling baik dan paling buruk sifatnya?',
        'Siapa mantan terindahmu?',
        'Siapa orang yang ingin kamu jadikan istri/suami?',
        'Apakah kamu pernah melakukan ghosting?',
        'Apa aib yang kamu sembunyikan dari teman-temanmu?',
        'Berapa jumlah mantanmu? sebutkan!',
    ]
tth = random.choice(t)

d = {'Lakukan rap gaya bebas selama 3 menit!':1, 
        'Biarkan orang lain membuat status menggunakan akun sosial mediamu!':2,
        'Berikan ponselmu kepada salah satu di antara kita dan biarkan orang tersebut mengirim satu pesan kepada siapapun yang dia mau!' :3,
        'Cium salah satu kaus kaki di antara temanmu!':4,
        'Makan satu gigitan kulit pisang!':5,
        'Peragakan salah satu orang di antara kita sampai ada yang bisa menebak siapa orang yang diperagakan!':6,
        'Nyanyikanlah salah lagu lagu dari Rossa!': 7,
        'Tirukan seorang selebriti sampai ada yang bisa menebak!':8,
        'Bertingkahlah seperti Hotman Paris selama 2 menit!':9,
        'Biarkan satu orang menggambar tato di wajahmu!':10,
        'Tutuplah mata lalu raba muka salah satu di antara kita sampai kamu bisa menebak siapa orang itu!':11,
        'Ungkapkan persaanmu kepada gebetanmu!':12,
        'Push up 20 kali!':13,
        'Kayang selama satu menit!':15,
        'Plank selama satu menit!.':16,
        'Coba teriak AKU SAYANG KAMU sekarang juga!':16,
        'Baca dengan lantang pesan yang terakhir kali kamu kirim ke gebetanmu!':17,
        'Telepon seorang teman dan katakan selamat ulang tahun sambil menyanyikan lagu!':18,
        'Tunjukkan gerakan dance terbaikmu!':19,
        'Parodikan adegan di film India kesukaanmu!':20,
        }
dare = random.choice(list(d.keys()))

g = ['https://i.pinimg.com/564x/d4/d0/4c/d4d04ca608a791e769fcef88c2435d6b.jpg', 
        'https://i.pinimg.com/564x/d5/00/4f/d5004fa2ded59ce5285a1eb7b9f00576.jpg',
        'https://i.pinimg.com/564x/53/ac/45/53ac458033d5f840800df3cd0b2ff55e.jpg',
        'https://i.pinimg.com/564x/e4/4d/2b/e44d2b46ace72839f413ecd2505acd3d.jpg',
        'https://i.pinimg.com/564x/1e/13/53/1e13536611cda462baa82113f9cadb3c.jpg',
        'https://i.pinimg.com/564x/9a/b7/6a/9ab76a96e274ebf97a1b74e53ae99a70.jpg',
        'https://i.pinimg.com/564x/76/10/1a/76101ab14bace1803bb37988c825e42a.jpg',
        'https://i.pinimg.com/564x/fe/61/5c/fe615cf92a1c99bfce7302adc44f4379.jpg',
        'https://i.pinimg.com/564x/d4/b7/3f/d4b73f7c2c470b02f1f1c3417fe616f7.jpg',
        'https://i.pinimg.com/564x/80/b6/c8/80b6c83d13ad4401ae92add70c393324.jpg',
    ]
gambar = random.choice(g)

s = [52002734, 
        52002735,
        52002736,
        52002737,
        52002738,
        52002740,
        52002748,
        52002745]
stiker = random.choice(s)

emoji = [
    {
        "index": 0,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "001"
    },
    {
        "index": 13,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "002"
    }
]

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'truth':
        message = TextSendMessage(tth + "\n" + "\n" + "Apakah bisa menjawabnya? Ketik 'bisa' jika memang bisa dan ketik 'gabisa' jika tidak mampu melakukannya")
        line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'dare':
        message = TextSendMessage(dare + "\n" + "\n" + "Apakah bisa melakukan tantangan ini? Ketik 'bisa' jika memang bisa dan ketik 'gabisa' jika tidak mampu melakukannya")
        line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'gabisa':
        line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url=gambar,
            preview_image_url='https://i.pinimg.com/564x/40/1e/cf/401ecf89c1d2cbac56d26cc95c3f9fb2.jpg'))
           
    if msg_from_user == 'berhenti':
        message = TextSendMessage(text='$ Terimakasih$', emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)
    
    if msg_from_user == 'aturan':
        line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url='https://i.pinimg.com/564x/53/25/ea/5325eab320dc87fcc72754708983abd4.jpg',
            preview_image_url='https://i.pinimg.com/564x/53/25/ea/5325eab320dc87fcc72754708983abd4.jpg'))


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
