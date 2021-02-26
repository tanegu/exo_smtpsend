import smtplib
from email.message import EmailMessage

# 接続先 SMTP サーバの定義
smtp = smtplib.SMTP('smtp.office365.com', 587)  # FQDN とポート番号

# 認証情報の定義
user = '.onmicrosoft.com'  # SMTP サーバに接続するためのユーザ
password = "XXXXXX"

# メッセージの組み立て
message = EmailMessage()
message['From'] = 'XXX'  # 送信者のメールアドレス
message['To'] = 'XXX'  # 受信者のメールアドレス
message['Subject'] = 'SUBJECT'  # 件名
message.set_content('CONTENT')  # 本文

smtp.ehlo()
    # (250, ...
smtp.starttls()  # TLS の開始（以降の通信は暗号化される）
    # (220, b'2.0.0 SMTP server ready') 
smtp.ehlo()
    # (250, ...
smtp.login(user, password)  # SMTP サーバにログイン
    # (235, ...
smtp.send_message(message)  # メッセージの送信
    # {}
smtp.quit()  # SMTP セッションの終了と TCP コネクションの切断
    # (221, b'2.0.0 Service closing transmission channel')


    #Office365からsmtpクライアントを使ってメール送信
    #http://honeotech.hatenablog.com/entry/2018/01/03/023911
    
