import requests

url = 'https://detik.com'
try:
    r = requests.get('%s' % url)
    print(f'Data : {r.text}')
except Exception as e:
    print('error : ', e)
