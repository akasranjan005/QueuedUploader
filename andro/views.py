from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from home.models import apkTable
from andro.models import apkPermission

def viewPermission(request):
  	return render_to_response('viewPermission.html', {'apkPermissions': apkPermission.objects.all() })

