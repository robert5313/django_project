from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

# Create your views here.
class TutorialView(APIView):

    serializers_class = TutorialSerializer

    def get(self, request):
        """
        Retrieves all the objects from the React model and returns a response containing the details of each object.

        Args:
            request: The request object containing information about the HTTP request.

        Returns:
            A list of dictionaries containing the details of each object from the React model.
            Each dictionary has keys "name" and "detail" representing the object's attributes.
        """
        details = [
            {"name": detail.name, "detail": detail.detail}
            for detail in Tutorial.objects.all()
        ]
        return Response["detail"]
    
    def post(self, request):
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    