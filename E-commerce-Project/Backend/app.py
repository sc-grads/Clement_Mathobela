from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pyodbc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@DESKTOP-LSF0DGJ/e-cormmerce?driver=SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    user_password = db.Column(db.String(50), nullable=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        user_password = request.form['password']
        new_customer = Customer(firstName=firstName, lastName=lastName, email=email, user_password=user_password)
        db.session.add(new_customer)
        db.session.commit()
        return 'Success'
    return render_template('sign_up.html')

if __name__ == '__main__':
    app.run(debug=True)
