import requests

# URL to randomuser.me API
url = "https://randomuser.me/api/"

# Send a GET request to the API
response = requests.get(url)
# Print the status code of the response.
print(response.status_code)