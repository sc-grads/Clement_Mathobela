from flask import request, jsonify

class Product:
    def insert_product(self):
        data = request.json
        name = data.get('name')
        brand = data.get('brand')
        description = data.get('description')
        picture = data.get('picture')
        color = data.get('color')
        stock = data.get('stock')
        price = data.get('price')
        # Insert product into the database
        db_manager.insert_product(name, brand, description, picture, color, stock, price)

        response = jsonify({'message': 'Product added successfully'})
        return response

    def delete_product(self):
        data = request.json
        name = data.get('name')
        color = data.get('color')
        db_manager.delete_product(name, color)
        response = jsonify({'message': 'Product successfully deleted'})
        return response

    def get_products(self):
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
