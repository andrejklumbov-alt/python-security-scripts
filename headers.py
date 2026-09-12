import requests

url_test = "https://httpbin.org"

data = {
    "X-Forwarded-For": "1.1.1.1"
}

res = requests.get(url_test, headers=data)

print(res.text)
