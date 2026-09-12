import requests

test_url = "https://google.com"

params = {"id": "' or 1=1 --"}

res = requests.get(test_url, params = params)

if res.status_code == 500:
    print("сайт неправильно проверил запрос возможенг SQL")
elif res.status_code == 404:
    print("страница не надена ")
elif res.status_code == 200:
    print("ответ впорядке уязвимости нет ")
else:
    print()
