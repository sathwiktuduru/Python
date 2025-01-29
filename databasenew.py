import mysql.connector
from mysql.connector import Error
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'TRIAL'
}

def create_db_connection(db_name=None):
    try:
        if db_name:
            DB_CONFIG['database']=db_name
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(e)
        return None

def create_database():
    connection = create_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            create_db_query = "CREATE DATABASE IF NOT EXISTS TRIAL;"
            cursor.execute(create_db_query)
            connection.commit()
            print("Database 'TRIAL' created successfully.")
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()
            connection.close()
            

 
def upload_csv_to_db(db_config):
    """
    Uploads data from a CSV file into a MySQL database.

    :param csv_file_path: The path to the CSV file
    :param db_config: Dictionary containing database connection info like user, password, host, database
    :return: None
    """
    s_name="Sathwik"
    s_roll=575
    s_dept="cse"
    grade="A"
    connection = create_db_connection()
    cursor = connection.cursor()
    query ="""INSERT INTO studentdetails (name, rollno, dept, grade) VALUES (%s, %s, %s, %s);"""
    cursor.execute(query, (s_name,s_roll,s_dept,grade))
    try:
        # Create a connection to the MySQL database
        connection = create_db_connection()

        if connection.is_connected():
            print("Successfully connected to the database")
            cursor = connection.cursor()

            # Create table if it doesn't exist
            create_table_query = """
                CREATE TABLE IF NOT EXISTS studentdetails (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(45),
                    rollno INT,
                    dept VARCHAR(10),
                    grade VARCHAR(1)
                )
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("Table studentdetails checked/created.")
    except Error as e:
        print(e)

def insert_student(name, rollno, dept, grade):
    """Inserts a single student record into the studentdetails table."""
    try:
        connection = create_db_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            query = """INSERT INTO studentdetails (name, rollno, dept, grade) VALUES (%s, %s, %s, %s);"""
            cursor.execute(query, (name, rollno, dept, grade))
            connection.commit()
            print(f"Record inserted: {name}, {rollno}, {dept}, {grade}")
    except Error as e:
        print(f"Error inserting record: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
                
insert_student("satwik",575,"cse","a")