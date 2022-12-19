
import requests


number_users = 5
# URL to randomuser.me API
url = f"https://randomuser.me/api?results={number_users}"

response = requests.get(url=url)
data=response.json()

results = data['results']

for user in results:
    print(user['name'])


