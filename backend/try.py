import mysql.connector
from mysql.connector import Error
import MySQLdb

try:
    print("Connecting to MySQL...")
    cnx = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd="root"
    )
    
    if cnx.is_connected():
        print("Connection successful!")
        cursor = cnx.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        print("Connected to database:", db_name[0])
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in the database:", tables)
        cursor.close()

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'cnx' in locals() and cnx.is_connected():
        cnx.close()
        print("Connection closed.")
