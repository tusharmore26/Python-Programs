import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root'
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

mycursor.execute("SELECT * FROM new ORDER BY name")

for x in mycursor:
    print(x)

#descending order
mycursor.execute("SELECT * FROM new ORDER BY name DESC")
result=mycursor.fetchall()
print(result)