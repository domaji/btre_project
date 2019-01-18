from django.contrib import admin
from listings.models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published','price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'price', 'address', 'city', 'state', 'zipcode')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)