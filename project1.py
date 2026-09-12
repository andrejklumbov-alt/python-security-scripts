import requests as re


url = "https://httpbin.org"

data = {
    "Agent-User": "1.1.1.1"
}
try:
    res = re.get(url,headers=data, timeout=3)
    if res.status_code == 200:
        print(f"сайт работает код: {res.status_code}")
    else:
        print(f"сайт не рабочий код: {res.status_code}")
except re.exceptions.Timeout:
    print("Превышено время ожидания ")
except re.exceptions.RequestException:
    print("Ошибка библеотеки")
except re.exceptions.ConnectionError:
    print("не удалось подключиться к серверу ")

