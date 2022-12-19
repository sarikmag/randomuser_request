<<<<<<< HEAD
import requests

number_users=5

url=f'https://randomuser.me/api/?results={number_users}'

response=requests.get(url)

data=response.json()

results=data['results']

for user in results:
    print(user['name']['first'],user['name']['last'])
=======

import requests
from user import User

number_users = 15
# URL to randomuser.me API
query_string = {
    'results':number_users,
    'gender':'female',
    'nat':"us,fr"
}
url = f"https://randomuser.me/api"

response = requests.get(url=url,params=query_string)
print(response.url)
data=response.json()

results = data['results']

for user in results:
    usr = User(user)
    print(usr.phone)


>>>>>>> fc0c115230951a537a38eb6cfacd871a28f4c196
