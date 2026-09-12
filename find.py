import requests

url = "https://google.com"

res = requests.get(url)

sec = res.text.lower().find("sql error")

if sec != -1:
    print("возможна ошибка в html")
else:
    print("такой строки не найдено")