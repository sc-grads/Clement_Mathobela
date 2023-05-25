from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from database_manager import DatabaseManager



app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:4200'])


##
db_manager = DatabaseManager(server='DESKTOP-LSF0DGJ', database='MobileStore')
##

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4200'
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    response.headers.add('Access-Control-Allow-Methods', 'OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


@app.route('/')
def home():
    return 'Welcome to the Flask app!'

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    # Insert user into database
    db_manager = DatabaseManager(server='DESKTOP-LSF0DGJ', database='MobileStore')

    db_manager.insert_user(email, first_name, last_name, password)

    response = jsonify({'message': 'Registered successfully'})
    return response


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Authenticate user with matching email and password
    db_manager = DatabaseManager(server='DESKTOP-LSF0DGJ', database='MobileStore')
    authenticated = db_manager.authenticate_user(email, password)


    # Check if user was authenticated
    if authenticated:
        # User is authenticated, return a success response
        return jsonify({'success': True, 'email': email})
    else:
        # User is not authenticated, return a failure response
        print('Invalid credentials')
        return jsonify({'success': False, 'error': 'Invalid credentials'})

@app.route('/getUserRole', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def get_user_role():
    email = request.args.get('email')
    db_manager = DatabaseManager(server='DESKTOP-LSF0DGJ', database='MobileStore')  
    user_role = None  # initialize user_role with None
    if email:
        user_role = db_manager.get_user_role(email)
    if user_role is not None:
        return jsonify({'user_role': user_role})
    return jsonify({'error': 'User not found'}), 404


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    data = request.json
    name = data.get('name')
    brand = data.get('brand')
    description = data.get('description')
    picture = data.get('picture')
    color = data.get('color')
    stock =data.get('stock')
    price = data.get('price')
    # Insert user into database
    db_manager = DatabaseManager(server='DESKTOP-LSF0DGJ', database='MobileStore')

    db_manager.insert_product(name,brand, description, picture, color, stock, price)

    response = jsonify({'message': 'Product added successfully'})
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    data = request.json
    name = data.get('name')
    color = data.get('color')

    # Assuming you have a DatabaseManager class that handles database operations
    db_manager = DatabaseManager(server='DESKTOP-LSF0DGJ', database='MobileStore')
    db_manager.delete_product(name, color)  # Pass both name and color parameters

    response = jsonify({'message': 'Product successfully deleted'})
    return response


@app.route('/products', methods=['GET'])
def get_products():
    rows = db_manager.get_products()
    products = []
    for row in rows:
        product = {
            'id': row[0],
            'name': row[1],
            'brand': row[2],
            'price': row[3],
            'description': row[4],
            'picture': row[5],
            'color': row[6],
            'stock': row[7]
        }
        products.append(product)
    return jsonify(products)


@app.route('/addToCart', methods=['GET','POST'])
def add_to_cart():
    data = request.json
    user_email = data.get('user_email')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    total_amount = data.get('total_amount')
    
    db_manager = DatabaseManager(server='DESKTOP-LSF0DGJ', database='MobileStore')

    user_id = db_manager.fetch_user_id(user_email)
    if user_id is None:
        return jsonify({'message': 'User not found'}), 404

    db_manager.add_to_cart(user_id, product_id, quantity, total_amount)

    response = jsonify({'message': 'Product added to cart successfully'})
    return response




@app.route('/delete-from-cart', methods=['POST'])
def delete_from_cart():
    data = request.json
    cart_id = data.get('cart_id')

    db_manager.delete_from_cart(cart_id)

    response = jsonify({'message': 'Item successfully deleted from cart'})
    return response

@app.route('/get-cart-items', methods=['POST'])
def get_cart_items():
    data = request.json
    user_id = data.get('user_id')

    cart_items = db_manager.get_cart_items(user_id)

    response = jsonify(cart_items)
    return response
    


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
