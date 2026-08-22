import os

from datetime import timedelta

import requests

PUSHOVER_TOKEN = os.environ["PUSHOVER_TOKEN"]
PUSHOVER_USER = os.environ["PUSHOVER_USER"]
JOB_STATUS = os.environ["JOB_STATUS"]
TTL = timedelta(hours=26) // timedelta(minutes=1)

payload = dict(
    token=PUSHOVER_TOKEN,
    user=PUSHOVER_USER,
    ttl=TTL,
    message=f"Workflow finished. {JOB_STATUS=}",
)
headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.post(
    "https://api.pushover.net/1/messages.json", headers=headers, data=payload
)
response.raise_for_status()
