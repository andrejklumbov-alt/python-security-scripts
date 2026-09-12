import json 
from concurrent.futures import ThreadPoolExecutor as thpool
import requests
import requests.exceptions as req_ex

def potoki(path):
    url = f"https://httpbin.org/{path}"
    try:
        res = requests.get(url, timeout=3)

        if res.status_code == 200:
            print("прошло")
        else:
            print("не прошло")
    except req_ex.RequestException:
        print("ошибка с склейкой url")
word_list = ["admin", "robots.txt", "login", "dashboard", "hidden_panel"]
print("запускаем потоки")
with thpool(max_workers=3) as ret:
    ret.map(potoki, word_list)
print("потоки начали работу")