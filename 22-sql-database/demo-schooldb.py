import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "schooldb"
    
)

mycursor = connection.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)