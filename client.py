import sys

import requests


response = requests.get("http://127.0.0.1:8080/")
print(response.text)

response_code = response.status_code
print(response_code)

if response_code == 200:
    print("All fine!")
else:
    sys.exit(1)



