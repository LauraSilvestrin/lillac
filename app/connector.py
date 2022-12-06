import mysql.connector
from mysql.connector import Error



def consultar(consulta):
    mycursor.execute(consulta)
    return(mycursor.fetchall())
    

mydb = mysql.connector.connect (
  host="127.0.0.1",
  user="root",
  password="abrl0404",
  database="projeto"
)

mycursor = mydb.cursor()