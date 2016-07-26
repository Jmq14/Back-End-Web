# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.template import RequestContext
from django import forms
from models import User
from django.core.mail import send_mail
from django.contrib.sites.models import Site
import random
import string
import os
from upload_avatar.app_settings import (
    UPLOAD_AVATAR_UPLOAD_ROOT,
    UPLOAD_AVATAR_AVATAR_ROOT,
    UPLOAD_AVATAR_RESIZE_SIZE,
)

from upload_avatar import get_uploadavatar_context


# RegUserForm
class RegUserForm(forms.Form):
	email = forms.EmailField(label='email:',widget = forms.EmailInput())
	name = forms.CharField(label='nickname',max_length=50)
	password = forms.CharField(label='password',widget=forms.PasswordInput())
	password_again = forms.CharField(label='password again',widget=forms.PasswordInput())

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email__exact=email):
			raise ValidationError('This email has been registered!')
		else:
			return email

	def clean_password_again(self):
		if self.cleaned_data.get('password_again') != self.cleaned_data.get('password'):
			raise ValidationError('Two passwords are not same!')
		else:
			return password_again


class LogUserForm(forms.Form):
	email = forms.EmailField(label='email:',widget=forms.EmailInput())
	password = forms.CharField(label='password',widget=forms.PasswordInput())

def login_required(func):
	def _deco(request):
		if request.COOKIES.get('login')=="True":
			return func(request)
		else:
			print request.COOKIES.get('login')
			return HttpResponse("please login first")
	return _deco

def activation_code(id,length=10):
    prefix = hex(int(id))[2:]+ 'L'
    length = length - len(prefix)
    chars=string.ascii_letters+string.digits
    return prefix + ''.join([random.choice(chars) for i in range(length)])

def active(request, activecode):
	user = User.objects.filter(activecode__exact=activecode)
	if user:
		user[0].is_active = True
		user[0].save()
		response = HttpResponseRedirect('/online/index')
		response.set_cookie('user',user[0].id,3600)
		response.set_cookie('login',True,3600)
		return response
	else:
		return HttpResponse('go to wrong page')

# regist
def regist(request):
	if request.method == 'POST':
		uf = RegUserForm(request.POST)
		if uf.is_valid():
			# retrieve the form data
			email = uf.cleaned_data['email']
			name = uf.cleaned_data['name']
			password = uf.cleaned_data['password']
			password_again = uf.cleaned_data['password_again']

			# add to the database
			user = User.objects.create(email = email, name = name, password = password, is_active = False)
			user.activecode = activation_code(user.id)
			user.save()
			send_mail(
				'welcome to convmusic!',
				'please click the link \nhttp://'+request.META['HTTP_HOST']+'/online/active/'+user.activecode+'/',
				'convmusic@126.com',
				[user.email],
				fail_silently=False,
			)
			response = HttpResponse('Please check your email')
			return response
	else:
		uf = RegUserForm()
	return render(request,'online/regist.html',{'uf':uf}, context_instance=RequestContext(request))


# login
def login(request):
	if request.method == 'POST':
		uf = LogUserForm(request.POST)
		if uf.is_valid():
			email = uf.cleaned_data['email']
			password = uf.cleaned_data['password']
			user = User.objects.filter(email__exact = email, password__exact = password, is_active__exact = True)
			if user:
				response = HttpResponseRedirect('/online/index')
				response.set_cookie('user',user[0],3600)
				response.set_cookie('login',"True",3600)
				return response
			else:
				uf.add_error(None,'wrong email or password!')
	else:
		uf = LogUserForm()
	return render(request,'online/login.html',{'uf':uf})

#login successfully
def index(request):
	user = request.COOKIES.get('user')
	user_id = request.COOKIES.get('user_id')
	user_name = request.COOKIES.get('user_name')
	if user_id:
		return render_to_response('online/index.html',{'login':True,'user_id':user_id,'user_name':user_name,'user':user}, context_instance=RequestContext(request))
	else:
		return render_to_response('online/index.html',{'login':False}, context_instance=RequestContext(request))

@login_required
def logout(requset):
	response = HttpResponseRedirect('/online/index')

	#clear cookie
	response.delete_cookie('user_id')
	response.delete_cookie('user_email')
	response.delete_cookie('user_name')
	response.delete_cookie('user')
	return response

@login_required
def find_content_type(filename):
    """In production, you don't need this,
    Static files should serve by web server, e.g. Nginx.
    """
    if filename.endswith(('.jpg', '.jpep')):
        return 'image/jpeg'
    if filename.endswith('.png'):
        return 'image/png'
    if filename.endswith('.gif'):
        return 'image/gif'
    return 'application/octet-stream'

@login_required
def get_upload_images(request, filename):
    content_type = find_content_type(filename)
    with open(os.path.join(UPLOAD_AVATAR_UPLOAD_ROOT, filename), 'r') as f:
        return HttpResponse(f.read(), content_type=content_type)

@login_required    
def get_avatar(request, filename):
    content_type = find_content_type(filename)
    with open(os.path.join(UPLOAD_AVATAR_AVATAR_ROOT, filename), 'r') as f:
        return HttpResponse(f.read(), content_type=content_type)

@login_required
def implement(request):
	u = User.objects.get(id=user_id)
	imgs = map(lambda size: "<p><img src='%s'/></p>" % u.get_avatar_url(size), UPLOAD_AVATAR_RESIZE_SIZE)
	html = """<html><body><h2>%s<a href="/online/upload">upload avatar</a></h2>%s</boby></html>""" % (request.user.username,'\n'.join(imgs))
	return HttpResponse(html)

@login_required
def upload(request):
    return render_to_response(
        'online/upload.html',
        get_uploadavatar_context(),
        context_instance = RequestContext(request)
    )






































# Create your views here.
