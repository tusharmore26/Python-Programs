import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root'
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

sql="DELETE FROM new WHERE name='Tushar'"
mycursor.execute(sql)

db.commit()

print(mycursor.rowcount,"row deleted!!")



