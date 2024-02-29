# file: appName/admin.py

from django.contrib import admin
from project.models import Book,Author,Custom # import the tables

# Register your models here.


admin.site.register(Book)


admin.site.register(Author)


admin.site.register(Custom)