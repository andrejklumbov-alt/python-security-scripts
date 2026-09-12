import requests

url_list = {
    "https://httpbin.org/status/500",
    "https://httpbin.org/status/403",
    "https://httpbin.org/status/404"
}

for codestatus in url_list:
    res = requests.get(codestatus)

    if res.status_code == 200:
        print(f"страниа ответила и работает {codestatus}")
    elif res.status_code == 403:
        print(f"фаервол нас заблокал {codestatus}")
    elif res.status_code == 404:
        print(f"такой страницы не существует {codestatus}")
    elif res.status_code == 500:
        print(f"ошибка на сервере {codestatus}")
    else:
        print("проверь URL на ошибки тк статус страницы не найден")
