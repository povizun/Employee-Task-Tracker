from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework.permissions import AllowAny
from django.urls import path

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]
