import mysql.connector 
from mysql.connector import Error

def create_connection(username, password, host):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )     
        if connection.is_connected():
            print("The MySQL connection")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None    

def create_database(connection, database_name):
    try:
        cursor = connection.cursor()
        query = f"CREATE DATABASE {database_name};"
        cursor.execute(query)
        print(f"Database '{database_name}' created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def create_table(connection, database_name, table_name, Columns):
    try:
        cursor = connection.cursor()
        connection.database = database_name
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({Columns});"
        cursor.execute(query)
        connection.commit()
        print(f"Table '{table_name}' created successfully in database '{database_name}'.")
        
    except Error as e:
        print(f"Error creating table: {e}")

def show_database(connection):
    try:
        cursor = connection.cursor()
        query = f"SHOW DATABASES;"
        cursor.execute(query)
        result = cursor.fetchall()
        
        print(f"\nDtabases: ")
        for row in result:
            print(row)
            
    except Error as e:
        print(f"Error showing databases: {e}")

def show_tables(connection, database_name):
    try:
        cursor = connection.cursor()
        connection.database = database_name
        query = f"SHOW TABLES;"
        cursor.execute(query)
        result = cursor.fetchall()
        
        print(f"\nTables: {database_name}")
        for row in result:
            print(row)
            
    except Error as e:
        print(f"Error showing tables: {e}")
        
