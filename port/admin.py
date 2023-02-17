from django.contrib import admin
from . models import Featured, Contact
# Register your models here.
admin.site.register(Featured)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'subject', 'sent']
