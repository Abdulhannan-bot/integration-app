from django.contrib import admin

# Register your models here.

from .models import Client, Signal

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email','password']
    search_fields = ['user','name']

admin.site.register(Client,ClientAdmin)

class SignalAdmin(admin.ModelAdmin):
    list_display = ['id','signal_type', 'stakeholder_current_company','stakeholder_first_name','stakeholder_last_name','stakeholder_current_title','stakeholder_time_in_current_role','stakeholder_current_email']
    search_fields = ['signal_type']

admin.site.register(Signal,SignalAdmin)