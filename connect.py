import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test"
)

print(mydb)

message=mydb.cursor()
message.execute("SELECT * FROM passwords")
view=message.fetchall()

for row in view:
    print(row)