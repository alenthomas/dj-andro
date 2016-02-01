from django.contrib import admin

from .models import Login, About, Team, Score


admin.site.register(Login)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Score)
