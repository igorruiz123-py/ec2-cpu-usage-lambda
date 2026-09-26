import json
import urllib.request
from cards import (
    build_alarm_card,
    build_ok_card
)
from os import getenv
from datetime import datetime
from zoneinfo import ZoneInfo

dict_ = {
    "i-0e340f85371539836": "cloudsocket-server"
}

TOKEN = getenv("TELEGRAM_TOKEN")
CHAT_ID = getenv("TELEGRAM_CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def lambda_handler(event, context):

    lambda_name = context.function_name

    timestamp = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%d/%m/%Y - %H:%M:%S")

    instance_name = None

    for i in dict_:

        if event["AlarmContributorAttributes"]["InstanceId"] == i:
            instance_name = dict_[i]
            break

        else:
            continue

    if event["NewStateValue"] == "OK":

        payload = build_ok_card(
            instance_name,
            timestamp,
            lambda_name,
            CHAT_ID
        )

    elif event["NewStateValue"] == "ALARM":

        payload = build_alarm_card(
            instance_name,
            timestamp,
            lambda_name,
            CHAT_ID
        )

    data = json.dumps(payload).encode('utf-8')

    request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")

    with urllib.request.urlopen(request) as response:

        if response.status == 200:
            print("Message sent successfully!")
        else:
            print(f"Error sending message: {response.status}")