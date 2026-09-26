def build_alarm_card(ec2_name, timestamp, lambda_function_name, chat_id):

    card = {
        "chat_id": f"{chat_id}",
        "text": f"🚨 **EC2 CPU Usage Alarm**\n\n EC2 instance running with CPU usage above 50%\n\n **Instance Name**: {ec2_name}\n\n **Date**: {timestamp}\n\n **Lambda Name**: {lambda_function_name}",
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Open AWS Console",
                        "url": "https://console.aws.amazon.com/"
                    }
                ]
            ]
        }
    }

    return card


def build_ok_card(ec2_name, timestamp, lambda_function_name, chat_id):

    card = {
        "chat_id": f"{chat_id}",
        "text": f"✅ **EC2 CPU Usage Alarm**\n\n EC2 instance returned to run with CPU usage under 50%\n\n **Instance Name**: {ec2_name}\n\n **Date**: {timestamp}\n\n **Lambda Name**: {lambda_function_name}",
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Open AWS Console",
                        "url": "https://console.aws.amazon.com/"
                    }
                ]
            ]
        }
    }
    
    return card