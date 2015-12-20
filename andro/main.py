import os
from androguard.core.bytecodes import apk
from xml.dom import minidom
from models import apkPermission

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def processApk(addr):
	app = apk.APK(addr)
	name = app.get_app_name()
	manif = app.get_android_manifest_axml()
	for permission in app.get_permissions():
		db = apkPermission(apkName = name, apkPermission = permission)
		db.save()
	return
