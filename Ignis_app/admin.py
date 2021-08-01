from django.contrib import admin
from Ignis_app.models import event

# Register your models here.
class eventAdmin(admin.ModelAdmin):
    list_display=['event_name','date','time','location','image','is_liked']
admin.site.register(event,eventAdmin)
