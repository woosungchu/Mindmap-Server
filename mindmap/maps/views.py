from rest_framework import viewsets, permissions
from maps.models import Map
from maps.serializers import MapSerializer

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
