# Tutorial working with requests

## Create a virtual environment

```bash
python3 -m venv venv
```

## Activate the virtual environment
for linux/mac

```bash
source venv/bin/activate
```

for windows

```bash
source venv\Scripts\activate
```

## Install the requirements

```bash
pip install -r requirements.txt
```

# Task 1

## Request the randomuser.me API

```python
import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

print(response.status_code)
print(response.text)
```

## Get 200 male users.

Make a request to the randomuser.me API and get 200 male users and save to JSON file.

JSON file structure:

```JSON
{
    "results":[
        {"first_name":"John", "last_name":"Doe","age":25},
        {"first_name":"User", "last_name":"User","age":21}
    ]
}

