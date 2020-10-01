from users.views import Dashboard, HomePage, Login, Registration, Logout


def initialize_users_routes(api):
    api.add_resource(HomePage, "/", methods=["GET"])
    api.add_resource(Registration, "/api/v1/registration", methods=["GET", "POST"])
    api.add_resource(Login, "/api/v1/login", methods=["GET", "POST"])
    api.add_resource(Logout, "/api/v1/logout", methods=["GET"])
    api.add_resource(Dashboard, "/api/v1/dashboard/<string:email>", methods=["GET"])
