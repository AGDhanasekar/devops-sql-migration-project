import mysql.connector
import time

print("Waiting for database...")
time.sleep(15)

connection = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="devops_db"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users")

result = cursor.fetchall()
print("Users:", result)

cursor.close()
connection.close()
