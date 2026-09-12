import requests as re
from concurrent.futures import ThreadPoolExecutor as thpool
def pool(pot):
    try:
        with open("url2.txt", "r") as file_search:
            for req in file_search:
                url = req.strip()
                if not url:
                    continue        
                res = re.get(url, timeout=3)
                if res.status_code == 200:
                    with open("url.txt", "a") as file_object:
                        file_object.write(url + "\n" )
                else:
                    print(f"сайт не рабочий {req} код: {res.status_code}")
           
    except re.exceptions.ConnectionError:
        print("не удалось подключиться")
    except re.exceptions.RequestException:
        print("Ошибка не удалось отправить запрос")
    except re.exceptions.Timeout:
        print("превышено время ожидания")
    print("проверка окончена ")


