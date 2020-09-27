from users.views import HomePgae, TestPost, TestGet


def initialize_users_routes(api):
    api.add_resource(HomePgae, "/", methods=["GET"])
    api.add_resource(TestPost, "/post/", methods=["POST"])
    api.add_resource(TestGet, "/get/<string:username>/", methods=["GET"])
