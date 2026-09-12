import requests

test_url = "https://httpbin.org"

test_passwords = ["1234", "12345", "qwerty", "correct_passwords"]

for passwords in test_passwords:
    form_data = {
        "username": "admin",
        "passwords": passwords
    }
    res = requests.post(f"{test_url}/post",data=form_data)

    print(f"Проверяем пароль {passwords} ответ сайта {res.status_code}")

    if passwords == "correct_paswords":
        print(f"пароль найден {passwords}")
        break 