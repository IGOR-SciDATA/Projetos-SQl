import requests

response = requests.get('http://127.0.0.1:5000/energia/demanda_mwhora/28397.099999970003')

if response.status_code == 200:
   message = response.json()
   print(message['energia'])
else:
    print(response.status_code)