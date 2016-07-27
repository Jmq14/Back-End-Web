from __future__ import unicode_literals

from django.db import models
from online.models import User
from music.models import Track
# Create your models here.

class Playlist(models.Model):
	name = models.CharField(max_length=50)
	owner = models.ForeignKey(User, related_name='created_list', null=True)
	pub_date = models.DateTimeField('date published')
	descript_txt = models.CharField(max_length=1000, null = True, blank = True)
	tracks = models.ManyToManyField(Track)
	marked_by = models.ManyToManyField(User, related_name='marked_list')

	def __unicode__(self):
		return self.name

	def __add__(self, Track):
		pass





