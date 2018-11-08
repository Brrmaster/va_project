from django.shortcuts import render

from artworks.models import Artwork
from artists.models import Artist


def index(request):
	artworks_for_sale = Artwork.objects.order_by('-listing_date').filter(is_sold=False)
	artworks_sold = Artwork.objects.order_by('-listing_date').filter(is_sold=True)
	artists = Artist.objects.order_by('-member_since')
	context = {
	'artworks_for_sale': artworks_for_sale,
	'artworks_sold': artworks_sold,
	'artists': artists
	}

	return render(request, 'pages/index.html', context);

