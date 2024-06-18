import os

import requests


PUSHOVER_TOKEN = os.environ["PUSHOVER_TOKEN"]
PUSHOVER_USER = os.environ["PUSHOVER_USER"]

payload = dict(
    token=PUSHOVER_TOKEN,
    user=PUSHOVER_USER,
    message="Workflow finished.",
    ttl=3600,
)
headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.post(
    "https://api.pushover.net/1/messages.json", headers=headers, data=payload
)
response.raise_for_status()
