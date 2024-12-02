import mysql.connector 
from mysql.connector import Error


def create_connection(username, password, host):
    global connection
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )
        
        if connection.is_connected():
            print("The MySQL connection")
            
    except Error as e:
        print(f"Error connecting to {e}")
    
    
create_connection("root", "500201", "localhost")
# create a database named 'aboud'

def create_database():
    