from flask import Flask, Response, request, jsonify, abort
from flask_restful import Resource, Api

from IO_LOTTERY.controllers import AddUserController, AddUserRequest

app = Flask(__name__)
api = Api(app)

users = []

class UserController(Resource):
    def post(self):
        dto = request.get_json()
        users.append(dto)
        return {"message": "User created", "data": dto}, 201

class OtherController(Resource):
    def post(self):
        raise NotImplementedError

api.add_resource(UserController, '/users')
api.add_resource(OtherController, '/other')

@app.errorhandler(NotImplementedError)
def handle_not_implemented_error(e):
    return {"message": "Not Implemented"}, 501

@app.route('/users', methods=['GET'])
def get_users():
    abort(501)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        abort(404)

    user.update(request.json)

    return jsonify(request.json), 200

@app.route('/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        abort(404)

    key = list(request.json.keys())[0]
    user[key] = request.json[key]

    return jsonify(request.json), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        abort(404)

    users.remove(user)

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
