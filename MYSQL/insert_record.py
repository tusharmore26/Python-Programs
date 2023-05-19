import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root',
    
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

sql="INSERT INTO new(name , age) VALUES (%s,%s)"
values=[
    ("Tushar",21),
    ("Vinit",21),
    ("Om",20),
    ("Prajwal",22),
    ("Yash",22)
]

mycursor.executemany(sql,values)

db.commit()

print(mycursor.rowcount,"record inserted!!")