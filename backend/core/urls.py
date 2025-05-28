from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from rest_framework.routers import DefaultRouter
from task.api.view import TaskViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

route = DefaultRouter()
route.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/user/', UserDetailsView.as_view(), name='user'),
    path('api/v1/', include(route.urls)),
]
