from django.db import models
from datetime import datetime
from artists.models import Artist

class Artwork(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length =75)
	artwork_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	price = models.IntegerField()
	is_sold = models.BooleanField(default=False)
	listing_date = models.DateTimeField(default=datetime.now, blank=True)
	description = models.TextField(blank=True)
	def __str__(self):
		return self.title


