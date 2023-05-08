from flask import jsonify, request, abort
from flask.views import MethodView
from flask_classful import FlaskView, route
from IO_LOTTERY.repositories import UserRepository

class UserView(FlaskView):
    def __init__(self):
        self.users = UserRepository()

    def index(self):
        abort(501)

    def post(self):
        user = request.json
        self.users.add(user)
        return jsonify(user), 201

    def put(self, user_id: int):
        user = self.users.get(user_id)
        if not user:
            abort(404)

        user.update(request.json)

        return jsonify(request.json), 200

    @route('/<int:user_id>', methods=['PATCH'])
    def partial_update(self, user_id: int):
        user = self.users.get(user_id)
        if not user:
            abort(404)

        key = list(request.json.keys())[0]
        user[key] = request.json[key]

        return jsonify(request.json), 200

    def delete(self, user_id: int):
        user = self.users.get(user_id)
        if not user:
            abort(404)

        self.users.delete(user)

        return '', 204
