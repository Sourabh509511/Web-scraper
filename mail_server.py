import smtplib

def send_mail(link):
    server=smtplib.SMTP('smtp.gmail.com',587)   #port number
    server.ehlo()
    server.starttls()   #puts smtp server in tls mode which means it will encrypt the smtp session
    server.ehlo()

    server.login('from','password')

    subject='Price fell down!'

    body='Check the price {}'.format(link)
    msg=f"Subject:{subject}\n\n{body}"
    print(body)
    print(msg)

    server.sendmail(
        'from',
        'to',
        msg
    )
