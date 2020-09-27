from flask import Response, request, jsonify
from flask_restful import Resource

from users.db.models import UserModel
import json


class HomePgae(Resource):
    def get(self):
        check_all_db = UserModel.objects.to_json()
        return Response(check_all_db, mimetype="application/json", status=200)


class TestPost(Resource):
    def post(self):
        data = json.loads(request.data)
        test_db = UserModel(**data).save()
        output = test_db.to_json()
        print(output)
        return Response(output, status=200)


class TestGet(Resource):
    def get(self, username):
        print(username)
        test_username = UserModel.objects.filter(username=username).to_json()
        print(test_username)
        return Response(test_username, mimetype="application/json", status=200)
