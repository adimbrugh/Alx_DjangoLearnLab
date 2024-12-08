
"""
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserProfileView
from django.urls import path, include


router = DefaultRouter()

router.register('register', RegisterView)
router.register('login', LoginView)
router.register('profile', UserProfileView)



urlpatterns = [] + router.urls
"""

from django.urls import path
from .views import RegisterView, LoginView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # User registration
    path('login/', LoginView.as_view(), name='login'),          # User login
    path('profile/', UserProfileView.as_view(), name='profile') # User profile management
]
