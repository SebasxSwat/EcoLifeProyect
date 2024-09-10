from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'  # Cambia esto por una clave segura
jwt = JWTManager(app)

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={
            'user_id': user.id,
            'is_admin': user.is_admin
        })
        return jsonify({
            'access_token': access_token,
            'is_admin': user.is_admin
        }), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401