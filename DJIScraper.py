import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import date

URL = "https://www.bestbuy.com/site/dji-mavic-2-pro-quadcopter-with-remote-controller-gray/6262620.p?skuId=6262620"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(class_="shop-product-title").get_text()
    price = soup.find(class_="priceView-customer-price").get_text()
    converted_price = float(price[1:6].replace(",", ""))

    if converted_price <= 1500:
        send_email()
    else:
        print(f"{date.today()} - price: ${converted_price}")


def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    subject = "Best Buy DJI Mavic Pro price is down!!!"
    body = "Check the Best Buy Link:  https://www.bestbuy.com/site/dji-mavic-2-pro-quadcopter-with-remote-controller-gray/6262620.p?skuId=6262620"

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail("4rabah@gmail.com", "rbabaci1@gmail.com", message)
    print("Hey, Email has been sent!")

    server.quit()


############  Run the script  ############
check_price()
