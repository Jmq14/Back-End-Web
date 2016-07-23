from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	email = models.EmailField(max_length=254)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	is_active = models.BooleanField(default=False)
	activecode = models.CharField(max_length=50,null=True)

	# don't know its work
	def __unicode__(self):
		return self.name
