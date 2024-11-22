from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from app.user.services import handle_login_register

User = get_user_model()


class LoginRegisterAPIView(APIView):

    class AuthTokenInputSerializer(serializers.Serializer):
        username = serializers.CharField(required=True, write_only=True)
        password = serializers.CharField(required=True, write_only=True)

    class AuthTokenOutputSerializer(serializers.Serializer):
        access_token = serializers.CharField()
        refresh_token = serializers.CharField()

    @extend_schema(
        summary=_("Generates an auth token"),
        request=AuthTokenInputSerializer,
        responses=AuthTokenOutputSerializer,
    )
    def post(self, request, *args, **kwargs):
        """
        Create a token for authentication.
        """
        serializer = self.AuthTokenInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user, tokens = handle_login_register(username, password)
        output_serializer = self.AuthTokenOutputSerializer(
            data=dict(
                access_token=tokens["access_token"],
                refresh_token=tokens["refresh_token"],
            )
        )
        output_serializer.is_valid(raise_exception=True)
        return Response(data=output_serializer.data)
