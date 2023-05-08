import pyodbc
import bcrypt

class DatabaseManager:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.connection_string = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;"
    
    def insert_user(self, email, first_name, last_name, password):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        # Rehash the password before inserting it into the database
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        query = f"INSERT INTO users (email, first_name, last_name, password) VALUES (?, ?, ?, ?)"
        cursor.execute(query, email, first_name, last_name, hashed_password)
        conn.commit()
        conn.close()


    def insert_product(self, name,brand, description, picture, color, stock,price):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = f"INSERT INTO products (name,brand, description, picture, color, stock,price) VALUES (?,?,?, (SELECT BulkColumn FROM OPENROWSET(BULK N'?', SINGLE_BLOB) AS picture),?,?,?)"
        cursor.execute(query,name,brand, description, picture, color, stock,price)
        conn.commit()
        conn.close()

    def get_user_role(self, email):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = "SELECT user_role FROM users WHERE email=?"
        cursor.execute(query, email)
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None
        else:
            return row[0]





    def authenticate_user(self, email, password):
        try:
            # connect to the database
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()

            # get the hashed password from the database
            query = f"SELECT password FROM users WHERE email='{email}'"
            cursor.execute(query)
            row = cursor.fetchone()
            hashed_password = row[0]

            # check the password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                return True
            else:
                return False

        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            # close the connection
            conn.close()


    
    
   
