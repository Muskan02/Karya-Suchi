from django.contrib import admin

from .models import Todo
from .models import theme
# Register your models here.

admin.site.register(Todo)
admin.site.register(theme)
