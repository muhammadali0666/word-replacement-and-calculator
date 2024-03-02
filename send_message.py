from credential import phone_number
import requests
import schedule
import time

def send_message():
  resp = requests.post("https://textbelt.com/text", {
    "phone": phone_number,
    "message": "hey",
    "key": "textbelt"
  })
  print(resp.json())

schedule.every(10).seconds.do(send_message)

while True:
  schedule.run_pending()
  time.sleep(1)
