from django.contrib import admin

# Register your models here.
from .models import BlogItem

admin.site.register(BlogItem)
