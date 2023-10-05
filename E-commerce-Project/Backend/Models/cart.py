
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