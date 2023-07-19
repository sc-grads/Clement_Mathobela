import pyodbc
import bcrypt
from decimal import Decimal


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

    def insert_product(self, name, brand, description, picture, color, stock, price):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = f"INSERT INTO products (name,brand, description, picture,price, color, stock) VALUES (?,?,?,?,?,?,?)"
        cursor.execute(query, name, brand, description, picture, price, color, stock)
        conn.commit()
        conn.close()

    def delete_product(self, name, color):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = "DELETE FROM products WHERE name = ? AND color = ?"
        cursor.execute(query, name, color)
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

    def fetch_user_id(self, email):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = "SELECT user_id FROM users WHERE email = ?"

        cursor.execute(query, (email,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return None

    def get_products(self):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
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

        ###Cart

    def fetch_user_id(self, email):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = "SELECT user_id FROM users WHERE email = ?"
        cursor.execute(query, email)
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return None

    def fetch_product_price(self, product_id):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = "SELECT price FROM products WHERE product_id = ?"
        cursor.execute(query, product_id)
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return None

    def get_product_id(self, name, color):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = "SELECT id FROM products WHERE name = ? AND color = ?"
        cursor.execute(query, name, color)
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return None

    def add_to_cart(self, user_id, product_id, quantity, total_amount):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()

        # Check if the product already exists in the cart for the user
        query = "SELECT * FROM cart WHERE user_id = ? AND product_id = ?"
        cursor.execute(query, user_id, product_id)
        existing_item = cursor.fetchone()

        if existing_item:
            # Product already exists in the cart, update the quantity and total amount
            existing_quantity = existing_item.quantity
            new_quantity = existing_quantity + quantity
            new_total_amount = existing_item.total_amount + Decimal(total_amount)

            update_query = "UPDATE cart SET quantity = ?, total_amount = ? WHERE cart_id = ?"
            cursor.execute(update_query, new_quantity, new_total_amount, existing_item.cart_id)
        else:
            # Product does not exist in the cart, insert a new item
            insert_query = "INSERT INTO cart (user_id, product_id, quantity, total_amount) VALUES (?, ?, ?, ?)"
            cursor.execute(insert_query, user_id, product_id, quantity, total_amount)

        conn.commit()
        conn.close()

    def fetch_product_details(self, product_id):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = """
        SELECT id, name, brand, price, description, picture, color, stock
        FROM products
        WHERE id = ?
        """
        cursor.execute(query, product_id)
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None
        else:
            product_details = {
                'id': row[0],
                'name': row[1],
                'brand': row[2],
                'price': row[3],
                'description': row[4],
                'picture': row[5],
                'color': row[6],
                'stock': row[7]
            }
            return product_details

    def get_cart_items(self, user_id):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()
        query = """
        SELECT c.cart_id, c.user_id, c.product_id, c.quantity, c.total_amount, p.name AS product_name, p.color, p.price
        FROM cart c
        JOIN products p ON c.product_id = p.id
        WHERE c.user_id = ?
        """
        cursor.execute(query, user_id)
        rows = cursor.fetchall()
        conn.close()
        return rows
