from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Healthcheck (pode ficar público)
    path('api/v1/health/', include('apps.health.urls')),

    # Autenticação (JWT)
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Usuários (API protegida)
    path('api/v1/users/', include('apps.accounts.urls')),
]
