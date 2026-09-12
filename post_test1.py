import requests

url = "https://httpbin.org/post"

form = {
    "name":"Artem",
    "passwords":"6767"
}

res = requests.post(url, data=form)

if res.status_code == 200:
    print("сайт работает")
else:
    print("проблема с url")

res2 = res.text.find("name")

if res2 != -1:
    print(res2)
else:
    print("такой строки нет")
print(res.text)