#Program: Get Exchange Rate
#Date: 2023.09.26

import requests

# Where CAD is the base currency and THB is the target currency you want to use
url = 'https://v6.exchangerate-api.com/v6/287aeae054b3dbf60085bd87/pair/CAD/THB'

# Making our request
response = requests.get(url)
data = response.json()

# Extract and print the conversion_rate
# conversion_rate = data['conversion_rate']
# cad2thb = print(f'$1 CAD = {conversion_rate} THB')
# print (cad2thb)

#Print all JSON data
print data