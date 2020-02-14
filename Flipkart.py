import requests
from bs4 import BeautifulSoup
from mail_server import send_mail

data=input(print("Enter the link of Flipkat product you want to tack: "))

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def check_price():
    page=requests.get(data,headers=header)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find('span',{'class':'_35KyD6'}).get_text()

    price=soup.find('div',{'class':"_1vC4OE _3qQ9m1"}).get_text()
    price1=price[1]
    price2=price[3:]
    cost=float(price1+price2)

    user_cost=float(input(print("Enter desired price for the product {}".format(title))))

    if(cost <= user_cost):
        send_mail(data)

