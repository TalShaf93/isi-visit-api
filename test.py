import requests

BASE = "http://127.0.0.1:5000/"


response = requests.post(BASE + 'visit', json = {"user_name":"test"})
print(response.json())

response = requests.get(BASE + 'visit')
print(response.json())

