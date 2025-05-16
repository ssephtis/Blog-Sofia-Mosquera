from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    CustomLogoutView,
    SignUpView,
    ProfileDetailView,
    ProfileUpdateView
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
]