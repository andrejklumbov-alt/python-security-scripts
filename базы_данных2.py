import sqlite3 as sql

reg = sql.connect("данные.db")
cursor = reg.cursor()
url = "https://htpbin.org"
status_code = "200"

cursor.execute(
    "INSERT INTO vulns (site, code) VALUES (?, ?)",
    (url, status_code)
)
reg.commit()
reg.close()
print("все добавленно")