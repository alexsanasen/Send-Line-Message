#Program: Get currect date & time
#Date: 2023.10.02

from datetime import datetime
import pytz

# Specify the PST timezone
pst_timezone = pytz.timezone('US/Pacific')

# Get the current date and format it
today_date = datetime.now(pst_timezone).strftime('%b %d, %Y PST@ %H:%M')

print(today_date)