from django.contrib import admin

from mailing.models import *


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('time', 'frequency', 'status')
    list_filter = ('time',)
    search_fields = ('status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('header', 'body')
    search_fields = ('header',)
