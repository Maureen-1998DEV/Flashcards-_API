from django.contrib import admin
from .models import Course,Note,Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Note)
