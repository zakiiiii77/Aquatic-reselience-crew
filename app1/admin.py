from django.contrib import admin
from . models import Articles

# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("Article_name","Article_number")

admin.site.register(Articles, ArticlesAdmin)
