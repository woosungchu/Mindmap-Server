from rest_framework import serializers
from maps.models import Map, Node
from django.contrib.auth.models import User

class MapUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username',)

class NodeSerializer(serializers.ModelSerializer):
    map = serializers.PrimaryKeyRelatedField(queryset=Map.objects.all())

    class Meta:
        model = Node
        fields = ('id','type','content','map',)

class MapSerializer(serializers.ModelSerializer):
    author = MapUserSerializer(required=False, allow_null=True)
    nodes = NodeSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Map
        fields = ('id','author','title','nodes','created',)
        depth = 1
