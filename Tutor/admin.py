from django.contrib import admin
from .models import *

class TutorAdmin(admin.ModelAdmin):
    filter_horizontal =('languages',)

# Register your models here.

admin.site.register(Tutor, TutorAdmin)
admin.site.register(Experience)
admin.site.register(Language)