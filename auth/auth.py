from fastapi_users.authentication import CookieTransport, BearerTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

cookie_transport = CookieTransport(cookie_max_age=3600)

SECRET = "SECRET"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)