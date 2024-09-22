from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
import bcrypt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
jwt = JWTManager(app)

# In-memory user storage (use a database in production)
users = {}


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = hashed_password
    
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username not in users:
        return jsonify({'message': 'User not found'}), 404
    
    if not bcrypt.checkpw(password.encode('utf-8'), users[username]):
        return jsonify({'message': 'Incorrect password'}), 401
    
    # Generate JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


if __name__ == '__main__':
    app.run(port=5001)
