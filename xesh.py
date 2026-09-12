import hashlib

a = input("введите название файла для проверки ")
b = input("введите хеш своего файла ")

with open(a, "rb") as file_object:
    file_bytes = file_object.read()

calculated_hash = hashlib.sha256(file_bytes).heshdigest()

if calculated_hash == b:
    print("файл проверен и безопасен")
else:
    print("хеши не совпали перепроверьте файл на изменения")