import datetime
import requests
import re
import json

url = ''
with open('url.txt') as file:  
    url = file.read() 

admin = ''
with open('admin.txt') as file:  
    admin = file.read() 

dowen_chat = admin

def say(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def run_command(command, params):
    if (command == "enter_dowen"):
        enter_dowen(params)
    if (command == "bot_talks"):
        bot_talks(params)

def enter_dowen(new_dowen):
    with open('dowens.json', 'r') as f:
        data = json.load(f)
    if str(new_dowen['message']['from']['id']) in data:
        say(new_dowen['message']['chat']['id'], "Я тебя уже знаю. Однако старый гей борозды не испортит")
    else:
        say(new_dowen['message']['chat']['id'], "Новым пидорам всегда рады! Я тебя запомнил")
        data[new_dowen['message']['from']['id']] = []
        with open('dowens.json', 'w') as outfile:
            json.dump(data, outfile)

def bot_talks(speech):
    print("talkin")
    if (str(speech['message']['from']['id']) != admin):
        return
    print("verified")
    say(dowen_chat, re.search('(\S*) (.*)',speech['message']['text']).group(2))