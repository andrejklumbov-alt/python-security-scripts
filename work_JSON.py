import requests as req

url = "https://google.com"

try:
    res = req.get(url)

    clear_url = res.json()
    print(clear_url)
except req.exceptions.JSONDecodeError:
    print("не json")
    print(f"статус сайта {res.status_code}")
    print(f"начало ответа {res.text[:100]}")