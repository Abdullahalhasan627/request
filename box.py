import My_SQL

connection = My_SQL.create_connection("root", "500201", "localhost")
# My_SQL.create_database(connection, "aboud")
# My_SQL.create_table(connection, "aboud", "pett", "ID INT, Name VARCHAR(20) NOT NULL, Age INT NOT NULL")
My_SQL.show_database(connection)
My_SQL.show_tables(connection, "aboud")
connection.close()