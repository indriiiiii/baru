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
ACCESS_TOKEN = '01L7Hdpb8jRSPSIxa6HCMl2jROgBghYejFeBOsuERxFT0TdTrIGs6bQyhFsUzgwFZ2AN/RDsjphX6+zNbWGeevSsckZKaqb2vccGf985lp93AjM/nKnS9D0wHVp+ObcAXXAptxv5WNqGUxKT+WfacgdB04t89/1O/w1cDnyilFU='
SECRET = '34aec7afc4e650d78fc16f4d908aedd0'
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
        'Ceritakan detail ciuman pertamamu…',
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

d = ['Lakukan rap gaya bebas selama 3 menit!', 
        'Biarkan orang lain membuat status menggunakan akun sosial mediamu!',
        'Berikan ponselmu kepada salah satu di antara kita dan biarkan orang tersebut mengirim satu pesan kepada siapapun yang dia mau!',
        'Cium salah satu kaus kaki di antara temanmu!',
        'Makan satu gigitan kulit pisang!',
        'Peragakan salah satu orang di antara kita sampai ada yang bisa menebak siapa orang yang diperagakan!',
        'Nyanyikanlah salah lagu lagu dari Rossa!',
        'Tirukan seorang selebriti sampai ada yang bisa menebak!',
        'Bertingkahlah seperti Hotman Paris selama 2 menit!',
        'Biarkan satu orang menggambar tato di wajahmu!',
        'Tutuplah mata lalu raba muka salah satu di antara kita sampai kamu bisa menebak siapa orang itu!',
        'Ungkapkan persaanmu kepada gebetanmu!',
        'Push up 20 kali!',
        'Kayang selama satu menit!',
        'Plank selama satu menit!.',
        'Coba teriak “aku sayang kamu” sekarang juga!',
        'Baca dengan lantang pesan yang terakhir kali kamu kirim ke gebetanmu!',
        'Telepon seorang teman dan katakan selamat ulang tahun sambil menyanyikan lagu!',
        'Tunjukkan gerakan dance terbaikmu!',
        'Parodikan adegan di film India kesukaanmu!',
    ]
dare = random.choice(d)

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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'mulai':
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Mau pilih apa?',
                actions=[
                    MessageTemplateAction(
                        label='Truth',
                        text='t'
                    ),
                    MessageTemplateAction(
                        label='Dare',
                        text='d'
                    )
                ]
            )
        )   
        line_bot_api.reply_message(event.reply_token, message)
        
    elif msg_from_user == 't':
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text= tth + "\n" + "\n"+ "Apakah bisa menjawabnya?"
            )
        )   
        line_bot_api.reply_message(event.reply_token, message)

    elif msg_from_user == 'd':
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text= dare + "\n"+ "\n"+ "Apakah bisa melakukannya?"
            )
        )   
        line_bot_api.reply_message(event.reply_token, message)
    
    elif msg_from_user == 'bisa':
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text= "coba ceritakan jawabanmu jika kamu memilih truth atau lakukan tantangan yang diberikan jika kamu memilih dare" + "\n"+ "\n"+ "Apakah ingin lanjut?",
                actions=[
                    MessageTemplateAction(
                        label='Lanjut',
                        text='mulai'
                    ),
                    MessageTemplateAction(
                        label='Berhenti',
                        text='berhenti'
                    )
                ]
            )
        )   
        line_bot_api.reply_message(event.reply_token, message)

    elif msg_from_user == 'gabisa':
        image_message = ImageSendMessage(
            original_content_url=gambar,
            preview_image_url='https://i.pinimg.com/564x/40/1e/cf/401ecf89c1d2cbac56d26cc95c3f9fb2.jpg'
            )
        line_bot_api.reply_message(event.reply_token, image_message) 
        
    elif msg_from_user == 'aturan':
        image_message = ImageSendMessage(
            original_content_url='https://i.pinimg.com/564x/53/25/ea/5325eab320dc87fcc72754708983abd4.jpg',
            preview_image_url='https://i.pinimg.com/564x/53/25/ea/5325eab320dc87fcc72754708983abd4.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
    elif msg_from_user == 'berhenti':
        sticker_message = StickerSendMessage(
            package_id='11537',
            sticker_id=stiker)
        line_bot_api.reply_message(event.reply_token, sticker_message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
