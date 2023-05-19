import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root'
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

sql="SELECT name FROM new WHERE name='Tushar'"
mycursor.execute(sql)

result=mycursor.fetchall()


print(result)


