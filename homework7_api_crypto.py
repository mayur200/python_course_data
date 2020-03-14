''''
Get the current rate of Ethereum and Bitcoin in doller and rupees using API

'''

# import urllib.request
import requests


import json

# def get_current_api(dlr):
# 	print(dlr)
# 	key = '37e1af6e637eb48ce1c5df540dc0e3f7'
# 	print(key)
# 	ids='BTC,ETH'
# 	interval='1d'
# 	convert = 'EUR'
# 	url = 'http://api.nomics.com/v1/markets?key='+key+'&ids='+ids+'&interval='+interval+'start=2020-03-07&convert='+convert
# 	response = urllib.request.urlopen(url).read()
# 	# print(response)
# 	jsonResponse = json.loads(response.decode('utf-8'))
# 	print(jsonResponse)


# 	# print(requests, ">>>>>>>>>>>>",response.text, type(response.text))



# print(get_current_api(10))l

key = '1f9711731ed59151e9d85ebb045744c6c18c48b30f676e32eb42b2e6e803fccd'

url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR&key='+key
response = requests.get(url)
rate = response.text
jsonResponse = json.loads(response.text)
print(jsonResponse)
btc = jsonResponse.get('BTC')







