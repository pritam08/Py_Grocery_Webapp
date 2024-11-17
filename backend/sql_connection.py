import datetime
import mysql.connector
import MySQLdb
__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = MySQLdb.connect(user='root', password='root', database='grocery_store')

  return __cnx

