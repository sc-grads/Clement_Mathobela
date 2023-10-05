# routes.py
from flask import jsonify, Flask, request
from flask_cors import cross_origin
from Controllers.user import User
from Controllers.product import Product
from Controllers.cart import Cart

app = Flask(__name__)


user_controller = User()
product_controller = Product()
cart_controller = Cart()

# User routes
@app.route('/register', methods=['POST'])
def register_route():
    response = user_controller.register()
    return response

@app.route('/login', methods=['POST'])
def login_route():
    response = user_controller.login()
    return response

@app.route('/fetchUserId', methods=['GET'])
def fetchUserId_route():
    response = user_controller.fetch_user_id()
    return response

@app.route('/getUserRole', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def getUserRole_route():
    response = user_controller.get_user_role()
    return response



# Product routes
@app.route('/insert_product', methods=['POST'])
def insert_product_route():
    response = product_controller.insert_product()
    return response

@app.route('/delete_product', methods=['POST'])
def delete_product_route():
    response = product_controller.delete_product()
    return response

@app.route('/get_products', methods=['GET'])
def get_products_route():
    response = product_controller.get_products()
    return response

# Cart routes
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart_route():
    response = cart_controller.add_to_cart()
    return response

@app.route('/update_cart_item', methods=['POST'])
def update_cart_item_route():
    response = cart_controller.update_cart_item()
    return response

@app.route('/remove_cart_item', methods=['POST'])
def remove_cart_item_route():
    response = cart_controller.remove_cart_item()
    return response

@app.route('/get_cart', methods=['GET'])
def get_cart_route():
    user_email = request.args.get('user_email')
    response = cart_controller.get_cart(user_email)
    return response


if __name__ == '__main__':
    app.run()
