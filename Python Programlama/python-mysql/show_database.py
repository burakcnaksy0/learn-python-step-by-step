import mysql.connector

mydatabase=mysql.connector.connect(
    host='127.0.0.1',
    # port
    user='root',
    password='1234',
)


mycursor=mydatabase.cursor()
mycursor.execute('show databases')

print('-----Mysql Sunucumdaki Veritabanlarim-----')

for databases in mycursor:
    print(databases)