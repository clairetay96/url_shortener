from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics, status
from .serializers import UrlSerializer, CreateShortenedUrlSerializer
from .models import Url
from rest_framework.views import APIView, exception_handler
from rest_framework.response import Response
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your views here.

def redirect_view(request, code):
	# Use the code to get the website
	website = Url.objects.filter(code=code)[0].url
	return HttpResponseRedirect(website)

class CreateUrlView(APIView):
	serializer_class = CreateShortenedUrlSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			website = serializer.data.get('url')

			validate = URLValidator()
			try:
				validate(website)
			except ValidationError:
				return Response(data="Invalid URL entered", status=status.HTTP_400_BAD_REQUEST)

			url = Url(url=website)
			url.save()

		return Response(UrlSerializer(url).data, status=status.HTTP_201_CREATED)


class UrlView(generics.ListAPIView):
	queryset = Url.objects.all()
	serializer_class = UrlSerializer