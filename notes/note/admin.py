from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Notes Admin"
admin.site.site_title = "Notes Admin Portal"
admin.site.index_title = "Welcome to Notes Portal"
admin.site.register(Notes)