from rest_framework import generics
from .models import *
from .serializers import *

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class User_roleListView(generics.ListCreateAPIView):
    queryset = User_role.objects.all()
    serializer_class = User_roleSerializer