import smtplib, ssl

def send_email(subject):
    host = "smtp.gmail.com"
    port = 465

    username = "raymondnnaji660@gmail.com"
    password = "kgtmtvjtyranyqne"

    receiver_email = "nnajiarinze001@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, subject)