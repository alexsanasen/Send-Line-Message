#Program: Send Exchange Rate CAD:THB to Line Messenger
#Date: 2023.09.26

import requests
import os
from datetime import datetime
from pytz import pytz

#Github Action secrets
KEY_EXCHANGERATE = os.environ.get('KEY_EXCHANGERATE')
KEY_LINETOKEN = os.environ.get('KEY_LINETOKEN')

# Get Exchange Rate CAD:THB
url = f'https://v6.exchangerate-api.com/v6/{KEY_EXCHANGERATE}/pair/CAD/THB'

# Making our request
response = requests.get(url)
data = response.json()

# Specify the PST timezone
pst_timezone = pytz.timezone('US/Pacific')

# Get the current date and format it
today_date = datetime.now(pst_timezone).strftime('%b %d, %Y PST@ %H:%M')

# Extract and print the conversion_rate
conversion_rate = data['conversion_rate']
cad2thb = f"\n{today_date}\n$1 CAD = {conversion_rate} THB"

# Line: Message Function
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

# Line: Notification Function
def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = KEY_LINETOKEN
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

#Line: Sending Message
lineNotify(cad2thb)