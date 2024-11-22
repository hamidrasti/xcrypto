from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from app.api.exceptions import APIError

User = get_user_model()


def handle_login_register(username, password) -> tuple:
    user = User.objects.filter(username=username).first()

    if not user:
        user = User.objects.create_user(username=username, password=password)

    if not user.check_password(password):
        raise APIError(
            cause=_("Invalid credentials."),
            extra={
                "error_code": 1001,
                "error_detail": "Invalid credentials.",
                "error_scope": APIError.Scope.AUTH,
            },
        )

    tokens = user.generate_tokens()
    return user, tokens
