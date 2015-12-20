import os
import sys
import django_rq
from django.shortcuts import redirect
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import django_rq
from django_rq import job
from andro import main
#from django.contrib.gis.utils import GeoIP
from django.template import  RequestContext
from ipware.ip import get_ip

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

loginAttempt=0;
incoming_ip=0;

def index(request):
	return render_to_response('appHome.html')

#def upload_file(request):
	

def uploadSuccess(request):
	def process(f):
			location = ROOT + '/apk/' + naem
			with open(location, 'wb+') as destinantion:
				for chunk in f.chunks():
					destinantion.write(chunk)
			django_rq.enqueue(main.processApk, location)
			@job
			def long_running_func():
			    pass
			long_running_func.delay()

			#temp = main.processApk(location)

	for nm,ak in enumerate(request.FILES.getlist("uploadFile")):
		naem = ak.name
		process(ak)
	
	return redirect('/home/')
	
	#print ak
	#location = ROOT + '/apk/' + filename +
	#	def process(file):
	#		location = ROOT


def login(request):
	ip = get_ip(request)
	if ip is not None:
		global loginAttempt
		loginAttempt = loginAttempt + 1

	if loginAttempt > 3:
		return HttpResponseRedirect('/blocked/', "error")
	else:
		return HttpResponse("the ip is" + " " + ip + " " + "the count is" + " " + str(loginAttempt))

def blocked(request):
	return HttpResponse("Your ID is Blocked<br><br>You are out of attempt and you must reset your password to continue!!!")
