"""
@Copyright Michelle Mark 2018
@author Michelle Mark

Admins for main pages including contact me
"""
from django.contrib import admin

from .models import ContactMe


class ContactMeFilter(admin.SimpleListFilter):
    title = 'Responded To'
    parameter_name = 'responded_to'

    def lookups(self, request, model_admin):

        return {
            ('NotRespondedTo', 'Not Responded To'),
            ('RespondedTo', 'Responded To'),
        }

    def queryset(self, request, queryset):

        if self.value() == 'NotRespondedTo':

            return queryset.filter(responded_to=False)

        if self.value() == 'RespondedTo':

            return queryset.filter(responded_to=True)


@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    fields = ['your_name', 'message', 'time_submitted', 'responded_to']
    list_display = ['responded_to', 'time_submitted', 'your_name']
    list_display_links = ['time_submitted', 'your_name']
    list_filter = [ContactMeFilter]
    readonly_fields = ['time_submitted']
    search_fields = ['your_name', 'message', 'time_submitted']
    ordering = ['-time_submitted', 'responded_to', 'your_name']
