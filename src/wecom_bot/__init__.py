import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()


def send_notice(title, subtitle):
    wecom_bot_key = os.getenv("WECOM_BOT_KEY")
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={wecom_bot_key}"
    headers = {'Content-Type': 'application/json'}
    current_time = datetime.now()
    # Format the time as "12:00:00"
    formatted_time = current_time.strftime("%H:%M:%S")
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f'''
{title}
> {subtitle}
> 时间: {formatted_time}
            ''',
            "mentioned_list": ["@all"],
        },
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.text)
