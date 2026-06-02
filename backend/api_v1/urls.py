from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import RegisterView, LoginView, UserProfileView, AdminOnlyView
from tasks.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/profile/', UserProfileView.as_view(), name='profile'),
    path('admin/users/', AdminOnlyView.as_view(), name='admin-users'),
    path('', include(router.urls)),
]