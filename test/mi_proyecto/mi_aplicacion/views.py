"""
Estas son las vistas blablabla
"""
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserListView(generics.ListCreateAPIView):
    """
    Esta es la vista para ver y crear usuarios.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Esta es la vista para ver, editar y eliminar un usuario específico.
    """
    #revisar primero si el usuario sesionado tiene permisos de eliminar (administrador).
    #se podrá borrar la cuenta?
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Listar y crear lugares

#ver detalles, editar y eliminar lugares

#Listar y crear categorias

#ver detalles, editar y eliminar categorias - no cualquiera podrá llegar a eliminar un lugar




