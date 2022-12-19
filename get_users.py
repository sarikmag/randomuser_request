
import requests


number_users = 5
# URL to randomuser.me API
query_string = {
    'results':number_users
}
url = f"https://randomuser.me/api"

response = requests.get(url=url,params=query_string)
data=response.json()

results = data['results']

for user in results:
    print(user['name'])


