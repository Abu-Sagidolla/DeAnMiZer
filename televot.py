import requests
from sys import argv
import os
import json



def send_msg(text):
	token = '' #add here your bot token
	chat_id = '' #here write a chat id where bot should send data
	url = 'https://api.telegram.org/bot' + token  +'/sendMessage'  + '?chat_id=' + chat_id + '&text=' + text
	result = requests.get(url)
	return result



def photo(x):
    token = ''
    chat_id = ''  
    url = 'https://api.telegram.org/bot' + token + '/sendPhoto'
    files = {'photo':open( x + '.png','rb')}
    data = {'chat_id':''}
    return requests.post(url,files = files,data = data).json()







