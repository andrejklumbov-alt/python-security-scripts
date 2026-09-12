import requests

tets = "https://google.com"

res = requests.get(f"{tets}")

if res.status_code == 200:
    print("Сайт существует")
else:
    print("Сайт не найден")
