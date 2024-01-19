from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserListView.as_view(), name='user-list'),
    path('user_role/', User_roleListView.as_view(), name='user_role-list'),
    # Agrega más URLs según sea necesario
]