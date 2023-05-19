import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root'
)

print(db)