import handlers
import requests
import re
import random_stuff

url = ''
with open('url.txt') as file:  
    url = file.read() 


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def dowen():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        upd = last_update(get_updates_json(url))
        if update_id == upd['update_id']:
            if (upd['message']['text'][0] == '/'):
                handlers.run_command(re.search('\S*',upd['message']['text'][1:]).group(0), upd)
            update_id += 1
    sleep(1)
 
if __name__ == '__main__':  
    dowen()
