from django.contrib import admin
from .models import package, user
# Register your models here.

admin.site.register(package)
admin.site.register(user)