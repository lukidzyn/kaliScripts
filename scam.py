import requests
import random
import json
import threading

url = 'https://olx.pl-havecash.xyz/getpayment/sms/715185148'
numOfThreads = 50

data = {
        'id': '715185148',
        'cardBalance': '',
        'fio': '',
        'cardNumber': '',
        'cardExp': '',
        'cardCvv': '',
}

def randCardNumber():
    cardNumber = ''

    for i in range(3):
        rand = random.randint(1111,9999)
        cardNumber = cardNumber + str(rand) + '+'

    rand = random.randint(1111,9999)
    cardNumber = cardNumber + str(rand)

    return cardNumber

def random_json_val(json_obj, k):
    return str(random.choice(json_obj))

names = json.loads(open('res/MaleNames.json').read())
surnames = json.loads(open('res/MaleSurnames.json').read())

def do_request():
    # for num in range(100):
    while(True):

        for name in names:
            data.update({
                'cardBalance': random.randint(100,9099),
                
                'fio': random_json_val(names, random.randint(1,554)) + '+' + random_json_val(surnames, random.randint(1,150000)),
                'cardNumber': randCardNumber(),
                'cardExp': str(random.randint(1,12)).zfill(2) + '/' + str(random.randint(21,32)),
                # 'cardMonth': str(random.randint(1,12)).zfill(2),
                # 'cardYear': random.randint(2021,2032),
                'cardCvv': random.randint(111,999),
            })

        response = requests.post(url, data=data).text
        print(response)
        print(data)

threads = []

for i in range(numOfThreads):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(numOfThreads):
    threads[i].start()

for i in range(numOfThreads):
    threads[i].join()
