import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=3306,
  user="root",
  password="1234",
  database="persondb"
)

mycursor = mydb.cursor()

sql = "insert into customers(customerName,customerDate) VALUES (%s,%s)"
val = (1, "Highway 21","5.9.2023",1)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")