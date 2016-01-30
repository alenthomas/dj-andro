from django.contrib import admin

from .models import Users
from .models import Comments

admin.site.register(Users)
admin.site.register(Comments)
