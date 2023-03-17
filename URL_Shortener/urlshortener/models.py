from django.db import models

# Create your models here.
class RandomUrl(models.Model):
	random_url_name = models.URLField(max_length=250, null=False, blank=False)

	def __str__(self):
		return self.random_url_name


class CustomUrl(models.Model):
	original_url_name = models.URLField(max_length=250, null=False, blank=False)
	custom_url_name = models.URLField(max_length=250, null=False, blank=False)

	def __str__(self):
		return self.custom_url_name

