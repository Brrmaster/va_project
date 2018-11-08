from django.db import models
from datetime import datetime
from artists.models import Artist

class Artwork(model.Model):
	artist = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length =75)
	price = models.DecimalField(decimal_place=2)
	is_sold = models.BooleanField(default=False)
	listing_date = models.DateTimeField(default=datetime.now, blank=True)
	description = models.TextField(blank=True)
	artwork_photo: models.ImageField(upload_to='photos/%Y/%m/%d/')
	def __str__(self):
		return self.title


