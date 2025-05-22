from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from rest_framework.routers import DefaultRouter

route = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/user/', UserDetailsView.as_view(), name='user'),
    path('api/v1/', include(route.urls)),
]
