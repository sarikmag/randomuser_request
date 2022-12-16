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
venv\Scripts\activate
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


