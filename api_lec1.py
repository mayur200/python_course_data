#read api from the www.weatherbit.io and print the tempreature from the API

import requests
import json

def get_current_temperature(city,postal_code):
	print(postal_code)
	key='111df503a6114f138be4910b1c125437'
	url = 'http://api.weatherbit.io/v2.0/current?city='+city+'&key='+key+'&postal_code='+str(postal_code)
	response = requests.get(url)
	print(requests, ">>>>>>>>>>>>",response.text, type(response.text))
	j_response = json.loads(response.text)
	print("***************************************************")
	# print("response>>>>>>>",j_response, type(j_response))
	print("***************************************************")
	current_temp = j_response['data'][0]['temp']
	uv_info = j_response['data'][0]['uv']
	print(uv_info)


	return current_temp






print(get_current_temperature('Mumbai',400065))