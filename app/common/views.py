from django.core.exceptions import (
    ValidationError as DjangoValidationError,
    PermissionDenied,
)
from django.http import Http404
from django.http import JsonResponse
from django.views.defaults import bad_request, page_not_found, server_error
from rest_framework import exceptions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import as_serializer_error
from rest_framework.views import exception_handler as base_exception_handler
from rest_framework_simplejwt.exceptions import InvalidToken

from app.api.exceptions import APIError
from app.common.exceptions import ApplicationError


def accepts_json(request):
    return request.META.get("HTTP_ACCEPT", "*/*").startswith("application/json")


def bad_request_handler(request, exception, *args, **kwargs):
    """
    Generic 400 error handler.
    """
    if accepts_json(request):
        data = {"message": "Bad Request (400)", "extra": {}}
        return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
    return bad_request(request, exception, *args, **kwargs)


def permission_denied_handler(request, exception, *args, **kwargs):
    """
    Generic 403 error handler.
    """
    if accepts_json(request):
        data = {"message": "Forbidden (403)", "extra": {}}
        return JsonResponse(data, status=status.HTTP_403_FORBIDDEN)
    return bad_request(request, exception, *args, **kwargs)


def not_found_handler(request, exception, *args, **kwargs):
    """
    Generic 404 error handler.
    """
    print("not_found_handler")
    if accepts_json(request):
        data = {"message": "Not Found (404)", "extra": {}}
        return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)
    return page_not_found(request, exception, *args, **kwargs)


def server_error_handler(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    if accepts_json(request):
        data = {"message": "Server Error (500)", "extra": {}}
        return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return server_error(request, *args, **kwargs)


def exception_handler(exc, ctx):
    """
    {
        "message": "Error message",
        "extra": {}
    }
    """
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = base_exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        if isinstance(exc, ApplicationError):
            data = {"message": exc.message, "extra": exc.extra}
            return Response(data, status=exc.status)

        return response

    if isinstance(exc.detail, (list, dict)):
        response.data = {"detail": response.data}

    if isinstance(exc, exceptions.ValidationError):
        response.data["message"] = "Validation error"
        response.data["extra"] = {  # NOQA
            "error_code": f"{APIError.Scope.VALIDATION}-4000",
            "error_detail": "Invalid input.",
            "fields": response.data["detail"],
        }
    elif isinstance(exc, InvalidToken):
        response.data["message"] = response.data["detail"].get("detail")
        response.data["extra"] = {}
    else:
        response.data["message"] = response.data["detail"]
        response.data["extra"] = {}

    del response.data["detail"]

    return response
