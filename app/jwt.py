from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_claims,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)


def assign_access_token(user, response):
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)


def unset_jwt(response):
    unset_jwt_cookies(response)
