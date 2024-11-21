from django.contrib import admin
from .models import Tweet ,Hashtag
# Register your models here.


admin.site.register(Hashtag)
admin.site.register(Tweet)