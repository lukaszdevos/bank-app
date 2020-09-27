from users.views import HomePage, Registration


def initialize_users_routes(api):
    api.add_resource(HomePage, "/", methods=["GET"])
    api.add_resource(Registration, "/registration/", methods=["GET", "POST"])
