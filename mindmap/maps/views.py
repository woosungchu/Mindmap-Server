from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from maps.models import Map
from maps.serializers import MapSerializer, UserSerializer

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self,serializer):
        User.objects.create_user(**serializer.validated_data)
