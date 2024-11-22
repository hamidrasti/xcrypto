from enum import StrEnum

from app.common.exceptions import ApplicationError


class APIError(ApplicationError):
    class Scope(StrEnum):
        AUTH = "auth"
        DEFAULT = "error"
        VALIDATION = "validation"
        EXCHANGE = "exchange"

    def __init__(self, cause, extra=None, status=None):
        error_extra = extra or {}

        error_code = getattr(cause, "code", None)
        error_detail = getattr(cause, "detail", None)

        error_cause_extra = getattr(cause, "extra", None) or {}
        error_response = error_cause_extra.get("response_data") or {}
        error_message = error_response.get("message") or ""

        error_scope = self.Scope.DEFAULT
        if isinstance(cause, str):
            error_scope = error_extra.pop("error_scope", None) or self.Scope.DEFAULT
            error_code = error_extra.pop("error_code", None)
            error_detail = error_extra.pop("error_detail", None)
            error_message = str(cause)

        super().__init__(
            message=error_message or "",
            status=status or 400,
            extra={
                **error_extra,
                "error_code": f"{error_scope}-{error_code or '0000'}",
                "error_detail": error_detail or "An error occurred.",
            },
        )
