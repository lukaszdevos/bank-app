from flask import Response, request, jsonify
from flask_restful import Resource

from users.db.models import User
import json


class HomePage(Resource):
    def get(self):
        test_username = User.objects().to_json()
        return Response(test_username, mimetype="application/json", status=200)


class Registration(Resource):
    def post(self):
        data = json.loads(request.data)
        register_user = User(**data).save()
        register_user.hash_password()
        register_user.save()
        output = register_user.to_json()
        return Response(output, status=200)
