from django.contrib import admin
from .models import RandomUrl, CustomUrl

# Register your models here.
admin.site.register(RandomUrl)
admin.site.register(CustomUrl)
