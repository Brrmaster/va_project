from django.contrib import admin

from .models import Artwork

class ArtworkAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'price', 'listing_date', 'is_sold', 'artist')
	list_filter = ('artist',)
	list_editable = ('is_sold',)
	search_fields = ('title', 'description', 'price')
	list_per_page = 25
admin.site.register(Artwork, ArtworkAdmin)
