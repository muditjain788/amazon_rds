#!/usr/bin/python3
import mysql.connector as mysql
# RDS info

user = "root"
pass = "password"
db = "name"
host = "endpoint on amazon"

# Now Connecting with Database
connection = mysql.connect(user=user,password=pass,database=db,host=host)

# Now Generating a sql lang cursor
cur = connection.cursor()

# Now we can write SQL Query
data = cur.execute("Select * from tables")
print(data)
