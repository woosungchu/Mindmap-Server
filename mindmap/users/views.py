from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self,serializer):
        User.objects.create_user(**serializer.validated_data)
