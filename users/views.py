import json

from flask import Response, jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from users.db.models import User
from app.jwt import assign_access_token, unset_jwt


class HomePage(Resource):
    @jwt_required
    def get(self):
        test_username = User.objects().to_json()
        return Response(test_username, mimetype="application/json", status=200)


class Registration(Resource):
    def post(self):
        data = json.loads(request.data)
        register_user = User(**data).save()
        register_user.hash_password()
        register_user.save()
        output = {
            "message": str(register_user.first_name).capitalize()
            + " "
            + str(register_user.last_name).capitalize()
            + " your bank account is created"
        }
        response = jsonify(output)
        response.status_code = 201
        return response


class Login(Resource):
    def post(self):
        data = json.loads(request.data)
        password = data["password"]
        user = User.objects(email=data["email"]).first()
        if user and user.check_password(password):
            output = {"message": "you are login successfully"}
            status_code = 202
            response = jsonify(output)

            assign_access_token(user, response)
        else:
            output = {"message": "your login details is incorrect"}
            status_code = 406
            response = jsonify(output)

        response.status_code = status_code

        return response


class Logout(Resource):
    @jwt_required
    def get(self):
        output = {"message": "you are log out"}
        status_code = 202

        response = jsonify(output)
        response.status_code = status_code
        unset_jwt(response)

        return response


class Dashboard(Resource):
    @jwt_required
    def get(self, email):
        user = User.objects(email=email).first()

        output = {"Cash balance": user.cash_bank}

        response = jsonify(output)
        response.status_code = 200

        return response