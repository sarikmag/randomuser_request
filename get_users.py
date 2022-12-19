import requests

number_users=5

url=f'https://randomuser.me/api/?results={number_users}'

response=requests.get(url)

data=response.json()

results=data['results']

for user in results:
    print(user['name']['first'],user['name']['last'])