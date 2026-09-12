import requests as req
from concurrent.futures import ThreadPoolExecutor as thpool
import sqlite3 as sql

def pool(url):
    try:
        res = req.get(url, timeout=3)
        if res.status_code == 200:
            ty = sql.connect("данные.db")
            cursor = ty.cursor()
            cursor.execute(f"INSERT INTO vulns (site, code) VALUES (?, ?)", (url, "200"))
            ty.commit()
            ty.close()
        else:
            print(f"сайт не рабочий код: {res.status_code}")
    except req.exceptions.ConnectionError:
        print("не удалось подключиться")
    except req.exceptions.RequestException:
        print("Ошибка не удалось отправить запрос")
    except req.exceptions.Timeout:
        print("превышено время ожидания")
url = []
with open("url2.txt", "r") as file_search:
    for ter in file_search:
        ret = ter.strip()
        if not ret:
            continue
        url.append(ret)
with thpool(max_workers=3) as pol:
    pol.map(pool, url)
ty2 = sql.connect("данные.db")
cursor2 = ty2.cursor()
cursor2.execute("SELECT * FROM vulns")
for row in cursor2:
    print(f"id {row[0]} | site {row[1]} | code{row[2]}")
cursor2.close()
print("програма закончила работу ")