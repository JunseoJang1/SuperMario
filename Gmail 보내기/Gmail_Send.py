import smtplib
import datetime as dt
import imghdr
import time
from email.mime.text import MIMEText

### 매일 발송 설정 ###
recipients = ['hismjhi@naver.com'] # 받는 사람(들)


title = '''제목''' # 제목
content = '''예약 발송 코딩 공부중''' # 메세지

Max = 1 # 보낼 메일의 양


Reservation = False # 예약 발송 설정
Timer = 1 # 예약 발송 시간 설정 ( 분 )


mail_id = 'junseo21g@gmail.com'
mail_pw = 'fdimdkaegikfhglh'
####################

x = dt.datetime.now()
if Reservation == True:
    MIN = Timer + x.minute

#### 메일 로그인 ####
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login(mail_id, mail_pw)

msg = MIMEText(content)
msg['Subject'] = title

with open ("logo.png", "rb") as image:
    image_file = image.read()

image_type = imghdr.what("logo", image_file)
msg.add_attachment(image_file, maintype = 'image', subtype = image_type)
####################

while Reservation:
    x = dt.datetime.now()
    if x.minute == MIN:
        for i in range (Max):
            recipient = recipients[i%len(recipients)]
            print("[ 매일 보내짐 ]\n\n받는 사람 : {0}\n제목 : {1}\n내용 : {2}".format(recipient, msg['Subject'], content))
            s.sendmail(mail_id, recipient, msg.as_string())
        s.close()
        Reservation = False

if Reservation == False:
    for i in range (Max):
        recipient = recipients[i%len(recipients)]
        print("[ 매일 보내짐 ]\n\n받는 사람 : {0}\n제목 : {1}\n내용 : {2}".format(recipient, msg['Subject'], content))
        s.sendmail(mail_id, recipient, msg.as_string())
    s.close()
        
