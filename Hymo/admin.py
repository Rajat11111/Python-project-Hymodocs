from django.contrib import admin
from .models import Doctors



admin.site.register(Doctors)


admin.site.site_header = "Hymo Admin"
admin.site.site_title = "Hymo Admin Portal"
admin.site.index_title = "Welcome to Hymo Admin Portal"
admin.site.site
