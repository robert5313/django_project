from rest_framework import serializers
from . models import *

class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['name', 'detail']