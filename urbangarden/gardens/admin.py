from django.contrib import admin

from .models import Garden,Resource, Category

admin.site.register(Garden)
admin.site.register(Resource)
admin.site.register( Category)
