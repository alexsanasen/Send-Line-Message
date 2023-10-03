#Program: Get currect date & time
#Date: 2023.10.02

from datetime import datetime

# Get the current date and format it
today_date = datetime.now().strftime('%b %d, %Y @ %H:%M')

print(today_date)