from rest_framework import serializers
from maps.models import Map, Node
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    #maps = MapSerializer(many=True)

    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('date_created', 'date_modified')

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node

class MapSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False, allow_null=True)
    nodes = NodeSerializer(many=True)

    class Meta:
        model = Map
        fields = ('id','author','title','nodes')#,'node','descript','path
        depth = 1
