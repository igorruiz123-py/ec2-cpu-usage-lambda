import json
import requests
from dotenv import load_dotenv
from os import getenv
from card import (
    build_alarm_card,
    build_ok_card
)
from datetime import datetime

load_dotenv("config/.env")
TELEGRAM_TOKEN = getenv("TOKEN")
TELEGRAM_CHAT_ID = getenv("CHAT_ID")
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

def lambda_handler():

    cpu_usage = int(input("enter CPU usage: "))

    if cpu_usage > 50:
        payload = build_alarm_card(
            "cloudsocket-server",
            datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
            "ec2-cpu-usage-lambda",
            TELEGRAM_CHAT_ID
        )
    else:
        payload = build_ok_card(
            "cloudsocket-server",
            datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
            "ec2-cpu-usage-lambda",
            TELEGRAM_CHAT_ID
        )

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("message sent to telegram bot")

    elif response.status_code == 404:
        print("failed to send message to telegram bot")

    else:
        print(json.dumps(response.json(), indent=4))

lambda_handler()
