from django.contrib import admin

from .models import Contact


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'date', 'name']
    list_filter = ['date']
    class Meta:
        model = Contact

admin.site.register(Contact, ContactModelAdmin)
