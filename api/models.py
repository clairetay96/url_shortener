from django.db import models
import string
import random

def generate_unique_code():
	length = 8

	while True:
		code = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=length))
		if Url.objects.filter(code=code).count() == 0:
			break

	return code


# Create your models here.
class Url(models.Model):
	url = models.CharField(max_length=2048, unique=False)
	code = models.CharField(max_length=30, default=generate_unique_code, unique=True)