# IMPORTS
from django.urls import path
from . import views

# APP NAME
app_name = 'users'

# URL PATTERNS
urlpatterns = [
    # Handles Login View
    path('', views.user_login, name='login'),
    # Handle Sign Up View
    path('signup/', views.user_signup, name='signup'),
    # Handles Profile View
    path('profile/', views.user_profile, name='profile'),
    # Handles User Authentication Logic
    path('auth/', views.user_authentication, name='auth'),
    # Handles User Logout Logic
    path('logout/', views.user_logout, name='logout'),
    # Handles User Delete Logic
    path('delete/', views.user_delete, name='delete'),

]