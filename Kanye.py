import smtplib
from email.message import EmailMessage
from typing import Dict
import schedule
import time 
import requests

def kanyeText():
    response = requests.get("https://api.kanye.rest")
    dict = response.json()
    return dict['quote']
    

def kanyeSend():

    with open("test.txt", "r") as a_file:
        for line in a_file:
            good_line = line.strip()
            space = good_line.index(" ")
            great_line = good_line[:space]
            print(great_line)
            
            msg = EmailMessage()
            msg.set_content(kanyeText())
            msg['subject'] = "Kanye said "
            msg['to'] = great_line

            user = "kanye.message.sabzz@gmail.com"
            password = "vnzimqhnriclming"

            msg['from'] = user

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
            server.quit()

# schedule.every().day.at("08:45").do(kanyeSend)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)


if __name__ == "__main__": 
    kanyeSend()

