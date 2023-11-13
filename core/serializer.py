from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']