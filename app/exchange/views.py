from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Crypto
from .services import ExchangeService

User = get_user_model()


class CreateOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    class CreateOrderInputSerializer(serializers.Serializer):
        crypto = serializers.SlugRelatedField(
            required=True,
            write_only=True,
            queryset=Crypto.objects.filter(is_active=True),
            slug_field="name",
        )
        amount = serializers.DecimalField(
            required=True, write_only=True, max_digits=24, decimal_places=8
        )

    class CreateOrderOutputSerializer(serializers.Serializer):
        access_token = serializers.CharField()
        refresh_token = serializers.CharField()

    @extend_schema(
        summary=_("Creates an order"),
        request=CreateOrderInputSerializer,
        responses=CreateOrderOutputSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = self.CreateOrderInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        crypto = serializer.validated_data["crypto"]
        amount = serializer.validated_data["amount"]

        user = request.user
        order = ExchangeService.create_order(user, crypto, amount)

        return Response(
            {
                "message": "Order created successfully",
                "order_id": order.id,
            },
            status=status.HTTP_201_CREATED,
        )
