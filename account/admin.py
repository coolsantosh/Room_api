from django.contrib import admin
from .models import User

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display=['id','name','email']

admin.site.register(User,userAdmin)
