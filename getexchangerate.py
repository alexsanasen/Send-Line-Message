#Program: Get Exchange Rate
#Date: 2023.09.26

import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/287aeae054b3dbf60085bd87/latest/CAD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print data