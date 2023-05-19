import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root'
)

mycursor=db.cursor()

mycursor.execute("CREATE DATABASE newdb")