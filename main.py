import requests

try:
    r = requests.get('https://goo gle.com')
    print(r.status_code)
except Exception as e:
    print('error : ', e)