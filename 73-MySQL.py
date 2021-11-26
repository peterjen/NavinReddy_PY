# https://www.youtube.com/watch?v=vR5utJvN4JY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=78
#  PROBLEM SOLVED : pip install mysql-connector-python

import mysql.connector
import json
my_db = mysql.connector.connect(host="localhost", user="peterjen", password="ptj10656", database="sql_hr")
my_cursor = my_db.cursor()

my_cursor.execute("show databases")

results = my_cursor.fetchall()

all_db = json.dumps(results,indent=2) # DUMP TO JSON STRING
print(results)                  # this is a list
print(type(results))
print(all_db)                   # this is a string
print(type(all_db))
# exit(0)


print("#####################")

my_cursor.execute("select * from employees;")

results = my_cursor.fetchall()          # CAN ONLY FETCH 1 TIME
all_db = json.dumps(results, indent=2)
# print(all_db)
# exit(0)

print(results)
# exit(0)
for i in my_cursor:
    print(i,"sssssssssssss")
# print(type(i))
my_db.close()

