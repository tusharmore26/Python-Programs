import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root'
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

sql="SELECT name FROM new"
mycursor.execute(sql)

result=mycursor.fetchone() #selecting first row
result2=mycursor.fetchall() #selecting all rows

print(result)
print(result2)

