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
    # Get the user's gender
    gender = results[0]['gender']

    # Return the user's name and age
    answer = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }
    return gender,answer



# Define users list
users = []

number_of_requests = 20
number_of_male=1
# Get 10 users
while number_of_male!=number_of_requests:
    # Get the user's name and age
    # Print request info
    

    gender,user = get_user_name()
    # Add the user to the list if the user male
    if gender=='male':
        print(f'Request: [{number_of_requests}/{number_of_male}]')
        users.append(user)

        number_of_male+=1

   
     
print(users)
