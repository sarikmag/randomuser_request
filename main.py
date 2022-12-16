import requests

def get_user_name():
    # URL to randomuser.me API
    url = "https://randomuser.me/api"
    # Send a GET request to the API
    response = requests.get(url)
    # Convert the response to JSON format
    data = response.json()
    # Get the results from the JSON data
    results = data["results"]
    # Get the first name
    first_name = results[0]["name"]["first"]
    # Get the last name
    last_name = results[0]["name"]["last"]
    # Get the age
    age = results[0]["dob"]["age"]

    # Return the user's name and age
    answer = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }
    return answer



# Define users list
users = []
number_of_requests = 10
# Get 10 users
for i in range(number_of_requests):
    # Get the user's name and age
    # Print request info
    print(f'Request: [{number_of_requests}/{i+1}]')
    user = get_user_name()
    # Add the user to the list
    users.append(user)

# Print the list of users
print(users)