from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def FBV_Profile(request):
    if request.method == "GET":
        profiles = profile.objects.all()
        serializer = SerializerPeofile(profiles,many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SerializerPeofile(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_Created)
        return Response(status=status.HTTP_404_NOT_FOUND)