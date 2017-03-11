from rest_framework import viewsets, permissions
from maps.models import Map, Node
from maps.serializers import MapSerializer, NodeSerializer
from maps.permissions import MapIsOwnerOrReadOnly, NodeIsOwnerOrReadOnly
from rest_framework import filters

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = (MapIsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('author',)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (NodeIsOwnerOrReadOnly,)

    # def get_queryset(self):
    #     """
    #     http://www.django-rest-framework.org/api-guide/routers/#usage
    #       api.register(r'nodes', NodeViewSet, 'node')
    #     bind with map
    #     """
    #     queryset = Node.objects.all()
    #     map = self.request.query_params.get('map_id', None)
    #     if map is not None:
    #         queryset = queryset.filter(map_id=map)
    #     return queryset
