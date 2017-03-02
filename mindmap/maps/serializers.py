from rest_framework import serializers
from maps.models import Map, Node
from django.contrib.auth.models import User

class MapUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('id','type','data')

class MapSerializer(serializers.ModelSerializer):
    author = MapUserSerializer(required=False, allow_null=True)
    nodes = NodeSerializer(many=True)

    class Meta:
        model = Map
        fields = ('id','author','title','nodes')
        depth = 1
