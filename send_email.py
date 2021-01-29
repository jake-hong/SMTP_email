from email.message import EmailMessage
import smtplib
import imghdr  # 이미지 확장자 파악해주는 모듈
import re

# SMTP 접속을 위한 서버, 계정 설정
SMTP_SERVER = "smtp.gmail.com"
# google의 SMTP server 포트 주소 설정
SMTP_PORT = 465


def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("이메일 발송완료")
    else:
        print("유효한 이메일 주소가 아닙니다.")


message = EmailMessage()
message.set_content("이메일 보내기 테스트 - 테스트1")

message["Subject"] = "메일 보내기 테스트입니다."
message["From"] = "#####@gmail.com"
message["To"] = "#####@gmail.com"

with open('sendemail/python.png', 'rb') as image:
    image_file = image.read()

image_type = imghdr.what('python', image_file)

# mixed 타입 이메일 보내기
message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("#####@gmail.com", "#####")
sendEmail("#####@gmail.com")
smtp.quit()
