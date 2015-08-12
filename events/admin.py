from django.contrib import admin
from .models import Event, Guest

class EventAdmin(admin.ModelAdmin):
    date_hiearchy = 'date_of_event'
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'event_start', 'event_end', 'time_of_event', 'month_event'),
        }),
        ('Event Details', {
            'fields': ('hosted_by', 'street_address', 'city', 'state', 'zip_code', 'telephone', 'category', 'month_event'),
            'classes': ('collapse',)
        })
    )
    list_display = ('title', 'event_start')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'hosted_by')


class GuestAdmin(admin.ModelAdmin):
    fields = ('event', 'user', 'attending_status', 'comment')
    list_display = ('user', 'attending_status')
    list_filter = ('attending_status',)
    search_fields = ('user', 'event')


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)