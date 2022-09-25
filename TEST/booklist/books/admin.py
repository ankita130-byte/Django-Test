from django.contrib import admin

# Register your models here.

# Import our Book model from our current directory
from .models import Book

# Register our Book Model in the Admin Panel
admin.site.register(Book)
