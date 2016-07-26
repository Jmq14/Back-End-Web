from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Playitem(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

	#def __beMarked__(self):

class Playlist(models.Model):
	name = models.CharField(max_length=50)
	owner_email = models.EmailField(max_length=254)
	owner_name = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	marked_num = models.BigIntegerField()
	descript_txt = models.CharField(max_length=1000)
	items = models.ManyToManyField(Playitem)

	def __unicode__(self):
		return self.name





