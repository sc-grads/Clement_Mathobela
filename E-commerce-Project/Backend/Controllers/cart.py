from flask import request, jsonify
import requests  

class Cart:
    def add_to_cart(self):
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

    def update_cart_item(self):
        data = request.json
        cart_id = data.get('cart_id')
        quantity = data.get('quantity')

        cart_item = db_manager.get_cart_item(cart_id)
        if cart_item is None:
            return jsonify({'message': 'Cart item not found'}), 404

        # Update the quantity and total_amount
        cart_item.quantity = quantity
        cart_item.total_amount = cart_item.price * quantity

        db_manager.update_cart_item(cart_id, quantity, cart_item.total_amount)

        return jsonify({'message': 'Cart item updated successfully'}), 200

    def remove_cart_item(self):
        email = request.args.get('email')

        if email is None:
            return jsonify({'error': 'Email parameter missing'}), 400

        response = requests.get('http://localhost:5000/fetchUserId', params={'email': email})

        if response.status_code == 200:
            user_id = response.json().get('user_id')
            db_manager.remove_cart_item(cart_id, user_id)
            cart_items = db_manager.get_cart_items(user_id)
            cart = []
            for item in cart_items:
                cart.append({
                    'cart_id': item.cart_id,
                    'user_id': item.user_id,
                    'product_id': item.product_id,
                    'quantity': item.quantity,
                    'total_amount': item.total_amount
                })
            return jsonify({'cart_items': cart}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    def get_cart(self, user_email):
        user_id = db_manager.fetch_user_id(user_email)
        if user_id is None:
            return jsonify({'message': 'User not found or cart is empty'}), 404

        cart_items = db_manager.get_cart_items(user_id)
        if cart_items is None:
            return jsonify({'message': 'Cart is empty'}), 404

        cart = []
        for item in cart_items:
            product_details = db_manager.fetch_product_details(item.product_id)
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
