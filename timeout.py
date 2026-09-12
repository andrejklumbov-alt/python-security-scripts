import requests  

url = "https://httpbin.org"

try:
    res = requests.get(url, timeout=2)
    print("успех сервер ответил")

except requests.exceptions.Timeout:
    print("ошибка сервер завис")

print(res.status_code)