from __future__ import unicode_literals

from django.db import models

from upload_avatar.signals import avatar_crop_done
from upload_avatar.models import UploadAvatarMixIn


# Create your models here.
class User(models.Model, UploadAvatarMixIn):
	email = models.EmailField(max_length=254)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	is_active = models.BooleanField(default=False)
	activecode = models.CharField(max_length=50,null=True)
	avatar_name = models.CharField(max_length=128,null=True)

	def get_uid(self):
		return self.id

	def get_avatar_name(self, size):
		return UploadAvatarMixIn.build_avatar_name(self, self.avatar_name, size)


	def save_avatar_in_db(sender, uid, avatar_name, **kwargs):
	    if User.objects.filter(id=uid).exists():
	        User.objects.filter(id=uid).update(avatar_name=avatar_name)
	    else:
	        User.objects.create(id=uid, avatar_name=avatar_name)

	avatar_crop_done.connect(save_avatar_in_db)
	# don't know its work
	def __unicode__(self):
		return "{\'id\':%s" % self.id+",\'name\':\'%s\'"%self.name+",\'email\':\'%s\'}"%self.email
