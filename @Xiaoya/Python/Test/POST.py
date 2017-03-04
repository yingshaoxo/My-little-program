import requests

r = requests.post('http://127.0.0.1:5000/Chat/', data = '1+1')
print(r.text)
