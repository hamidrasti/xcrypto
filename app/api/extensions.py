from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object


class UserAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = "app.user.authentication.UserAuthentication"
    name = "UserAuthentication"
    match_subclasses = True
    priority = -1

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix=self.target.keyword,
        )
