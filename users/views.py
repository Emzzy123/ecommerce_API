# users/views.py
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
