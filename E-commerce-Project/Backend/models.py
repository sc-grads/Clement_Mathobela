from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.String(50))

    def __repr__(self):
        return f"Customer(customer_id={self.customer_id}, firstName='{self.firstName}', lastName='{self.lastName}', email='{self.email}', user_password='{self.user_password}')"
