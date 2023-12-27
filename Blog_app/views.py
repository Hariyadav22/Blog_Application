from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Blog, Points
from .serializers import BlogSerializer, pointSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class PointViewSet(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = pointSerializer

@api_view(['GET',])
def catagory_details(request,slug):
    try:
        tasks=Blog.objects.filter(slug=slug)
        print(tasks)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serialized_task=BlogSerializer(tasks,many=True)
        return Response(serialized_task.data)

