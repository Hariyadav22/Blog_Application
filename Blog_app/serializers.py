from rest_framework import serializers
from .models import Blog, Points

class pointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    points = pointSerializer(many=True)
    class Meta:
        model = Blog
        fields = '__all__'



    