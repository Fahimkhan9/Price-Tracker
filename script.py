import requests
from bs4 import BeautifulSoup
import smtplib
import text_to_speech as speech
import time
URL = "https://www.rokomari.com/book/202772/hate-kolome-javascript"

headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36" }

def  find_price():

    page =  requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    price = soup.find("span", {"class": "sell-price"}).get_text()
    # print(soup.prettify())

    convertedprice = float(price[4:])


    if convertedprice > 300:
        speech.speak("Hey Alif you can buy this", "en")
    

    print(convertedprice)


while True:

    find_price()
    time.sleep(60*60)
