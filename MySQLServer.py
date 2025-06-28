import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nzisa@1999pujo",
        database="alx_book_store"
    )

    mycursor = mydb.cursor()
    print("Database 'alx_book_store' created successfully!")
    
except:
    print("Error: Connection failed!")

mycursor.close()
mydb.close()
