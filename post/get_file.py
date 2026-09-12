import requests

with open("67.txt", "r") as file_object:
    for les in file_object:

        url = les.strip()

        print(url)

        res = requests.get(url)

        if res.status_code == 200:
            print("получилось")
        else:
            print("что-то  не так")