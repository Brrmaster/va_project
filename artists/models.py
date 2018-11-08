from django.db import models
from datetime import datetime

class Artist(models.Model):
	name = models.CharField(max_length=50)
	biography = models.TextField(blank=True)
	artist_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	member_since = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.name