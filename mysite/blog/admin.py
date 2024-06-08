from django.contrib import admin
from . import models

# Register your models here.

class Authoradmin(admin.ModelAdmin):
    list_display=('title','slug', 'author')
admin.site.register(models.Post, Authoradmin)
#the author admin and model admin classes are used to describe the appearance on the django admin site