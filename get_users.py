
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


