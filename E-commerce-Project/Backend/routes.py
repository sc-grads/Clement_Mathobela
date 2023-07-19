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
    db_manager = DatabaseManager(server='DESKTOP-LSF0DGJ', database='MobileStore')
    db_manager.delete_product(name, color)
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

@app.route('/fetchUserId', methods=['GET'])
def fetch_user_id():
    email = request.args.get('email')
    user_id = db_manager.fetch_user_id(email)
    if user_id is None:
        return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify({'user_id': user_id}), 200

@app.route('/addToCart', methods=['POST'])
def addToCart():
    data = request.json
    user_email = data.get('user_email')
    product_name = data.get('product_name')
    product_color = data.get('product_color')
    quantity = data.get('quantity')
    total_amount = data.get('total_amount')

    # Fetch the product_id using the product_name and product_color
    product_id = db_manager.get_product_id(product_name, product_color)
    if product_id is None:
        return jsonify({'message': 'Product not found'}), 404

    # Fetch the user_id using the user_email
    user_id = db_manager.fetch_user_id(user_email)
    if user_id is None:
        return jsonify({'message': 'User not found'}), 404

    # Add the item to the cart
    db_manager.add_to_cart(user_id, product_id, quantity, total_amount)

    return jsonify({'message': 'Item added to cart'}), 200

@app.route('/cart/<string:user_email>', methods=['GET'])
def getCart(user_email):
    user_id = db_manager.fetch_user_id(user_email)
    if user_id is None:
        return jsonify({'message': 'User not found or cart is empty'}), 404
    else:
        cart_items = db_manager.get_cart_items(user_id)
        if cart_items is None:
            return jsonify({'message': 'Cart is empty'}), 404
        else:
            cart = []
            for item in cart_items:
                product_id = item.product_id
                product_details = db_manager.fetch_product_details(product_id)
                if product_details is None:
                    # Handle the case when the product details are not found
                    return jsonify({'message': 'Product details not found'}), 404

                cart.append({
                    'cart_id': item.cart_id,
                    'user_id': item.user_id,
                    'product_id': item.product_id,
                    'quantity': item.quantity,
                    'total_amount': item.total_amount,
                    'product_name': product_details['name'],
                    'product_color': product_details['color'],
                    'price': product_details['price'],
                    'product_picture': product_details['picture']
                })
            return jsonify(cart), 200


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
