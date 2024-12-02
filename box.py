import mysql.connector 
from mysql.connector import Error

def create_connection(username, password, hostname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

create_database = "CREATE DATABASE aboud;"

# def create_table():

create_connection("root", "500201", "localhost")