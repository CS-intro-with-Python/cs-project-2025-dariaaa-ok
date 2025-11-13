import sys

import requests

OK, ERR, RST = "\033[32m", "\033[31m", "\033[0m"

response = requests.get("http://127.0.0.1:8080/")
print(response.text)

response_code = response.status_code
print(response_code)

if response_code == 200:
    print(f"{OK}All fine!{RST}")
    print("::notice title=Healthcheck passed::")
else:
    print(f"{ERR}Something went wrong!{RST}")
    print("::error title=Healthcheck failed::")
    sys.exit(1)



