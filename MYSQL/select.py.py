import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root'
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

sql="SELECT * FROM new"
mycursor.execute(sql)

for x in mycursor:
    print(x)