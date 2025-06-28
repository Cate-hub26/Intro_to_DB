import mysql.connector

"CREATE DATABASE IF NOT EXISTS alx_book_store;"

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nzisa@1999pujo",
    )

    mycursor = mydb.cursor()
    print("Database 'alx_book_store' created successfully!")
    
except:
    print("Error: Connection failed!")

mycursor.close()
mydb.close()
