import requests
import re

host, port = "94.237.61.82", 44246
url = f"http://{host}:{port}"

login = {
    "name":"test"
}

response = requests.post(f"{url}",data=login)

flag = re.search(r'HTB\{.*\}',response.text)
print(flag.group(0))