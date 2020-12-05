import requests,json


info = requests.get('http://ipinfo.io/json').json()

ip_address = info['ip']
city = info['city']
location = info['loc']


