from django.urls import path

from app.user.views import LoginRegisterAPIView

urlpatterns = [
    path("login/", LoginRegisterAPIView.as_view(), name="login"),
]
