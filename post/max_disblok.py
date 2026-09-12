import requests as re

print("начинаем скан урл из файла")

with open("67.txt", "r") as file_object:
    for les in file_object:
        url = les.strip()
        if not url:
            continue
        try:
            res = re.get(url,timeout=3)

            if res.status_code == 200:
                print(f"получилось {les}")
                with open("52.txt", "a") as out_file:
                    out_file.write(url + "\n"  )
            else:
                print(f"неполучилось {les}")
        except re.exceptions.Timeout:
            print("время обработки вышло")
        except re.exceptions.ConnectionError:
            print("не получилось подключиться")
        except re.exceptions.RequestException:
            print("ошибка библеотеки")
print("сканирование завершено ")


        