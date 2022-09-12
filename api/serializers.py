from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Url
		fields = ('id','url','code')

class CreateShortenedUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Url
		fields = ['url']