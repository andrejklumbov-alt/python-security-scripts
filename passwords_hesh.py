import hashlib

passwords = input("напиши свой пароль ")

text_bytes = passwords.encode("utf 8")

hash_object = hashlib.sha256(text_bytes)

hash = hash_object.hexdigest()

print(f"вот твой хеш {hash}")