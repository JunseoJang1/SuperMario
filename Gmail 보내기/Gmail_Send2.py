import smtplib
from email.message import EmailMessage
import imghdr

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("네이버.")

message["Subject"] = "[Naver] Look!" # 제목
message["From"] = "junseo21g@gmail.com" # 보낸 사람
message["To"] = "junseo21g@gmail.com" # 받는 사람

with open("logo.png", "rb") as image:
    image_file = image.read()

image_type = imghdr.what('logo', image_file)
message.add_attachment(image_file, maintype = 'image', subtype = image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("junseo21g@gmail.com", "fdimdkaegikfhglh")
smtp.send_message(message)
smtp.quit()
