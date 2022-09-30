from django.contrib import admin
from .models import Base, Comment

# Register your models here.
admin.site.register(Base)
admin.site.register(Comment)