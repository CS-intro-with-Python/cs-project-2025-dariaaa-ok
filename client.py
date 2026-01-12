import sys
import requests

OK, ERR, RST = "\033[32m", "\033[31m", "\033[0m"

base_url = "http://127.0.0.1:8080"
    # "https://cs-project-2025-dariaaa-ok-production.up.railway.app"

routes = ["/", "/dogs", "/cats", "/dogs/add", "/cats/add"]

for route in routes:
    response = requests.get(base_url + route)
    print(response.text)
    print(response.status_code)

    if response.status_code == 200:
        print(f"{OK}{route} is OK!{RST}")
        print("::notice title=Healthcheck passed::")
    else:
        print(f"{ERR}{route} failed!{RST}")
        print("::error title=Healthcheck failed::")
        sys.exit(1)

print(f"{OK}All checked routes are OK!{RST}")
