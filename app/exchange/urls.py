from django.urls import path

from app.exchange.views import CreateOrderAPIView

urlpatterns = [
    path("create-order/", CreateOrderAPIView.as_view(), name="create_order"),
]
