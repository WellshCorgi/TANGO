"""
high level support for doing this and that.
"""
from rest_framework import serializers

from .models import Node
from .models import Edge
from .models import Pth


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = '__all__'


class PthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pth
        fields = '__all__'