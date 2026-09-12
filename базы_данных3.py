import sqlite3 as sql
reg = sql.connect("данные.db")
cursor = reg.cursor()

cursor.execute("SELECT * FROM vulns")

ter = cursor.fetchall()

for row in ter:
    print(f"id {row[0]} | site {row[1]} | code{row[2]}")
reg.close()