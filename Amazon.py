import requests
from bs4 import BeautifulSoup
from mail_server import send_mail

data=input(print("Enter the link of Amazon product you want to tack: "))



header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def check():
    page=requests.get(data,headers=header)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id='productTitle').get_text()

    price=soup.find(id="priceblock_dealprice").get_text()

    cost1=price[2]
    cost2=price[4:6]
    cost=float(cost1+cost2)


    user_price=float(input(print("Enter the price you want for the product {}".format(title.strip()))))

    if (cost <= user_price):
        send_mail(data)

