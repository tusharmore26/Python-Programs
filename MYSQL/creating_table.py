import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root',
    
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

mycursor.execute("CREATE TABLE new(name varchar(20), age int(3))")

