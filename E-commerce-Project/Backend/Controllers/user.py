from flask import request, jsonify

class User:
    def register(self):
        print("running")
        
        data = request.json
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        db_manager.insert_user(email, first_name, last_name, password)

        response = jsonify({'message': 'Registered successfully'})
        return response

    def login(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Authenticate user with matching email and password
        authenticated = db_manager.authenticate_user(email, password)

        # Check if user was authenticated
        if authenticated:
            # User is authenticated, return a success response
            return jsonify({'success': True, 'email': email})
        else:
            # User is not authenticated, return a failure response
            print('Invalid credentials')
            return jsonify({'success': False, 'error': 'Invalid credentials'})

    def fetch_user_id(self):
        email = request.args.get('email')
        user_id = db_manager.fetch_user_id(email)
        if user_id is None:
            return jsonify({'message': 'User not found'}), 404
        else:
            return jsonify({'user_id': user_id}), 200

    def get_user_role(self):
        email = request.args.get('email')
        user_role = None  # initialize user_role with None
        if email:
            user_role = db_manager.get_user_role(email)
        if user_role is not None:
            return jsonify({'user_role': user_role})
        return jsonify({'error': 'User not found'}), 404
