# https://www.youtube.com/watch?v=vR5utJvN4JY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=78
#  PROBLEM SOLVED : pip install mysql-connector-python

import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", password="ptj10656", database="sql_hr")
my_cursor = my_db.cursor()
my_cursor.execute("select * from employees;")

results = my_cursor.fetchall()
#print(type(results))

my_cursor.execute("select * from employees;")
for i in my_cursor:
    print(i)
print(type(i))
my_db.close()