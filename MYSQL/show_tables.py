import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root',
    
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)


