import sqlite3
conection = sqlite3.connect("данные.db")

cursor = conection.cursor()
print("сoздаем таблицу")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vulns(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site TEXT,
    code TEXT
)
""")
conection.commit()

conection.close()
print("файл создан")

