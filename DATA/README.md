AppWatch
========

A short description of the project.

This Project uses Mysql as Database.

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* MySQL

Install the global dependencies using `packages.txt`::
    
    $ apt-get install $(cat packages.txt)

Make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Configure all the paths in settings.py respectively, some of the sample paths are below::
    
    ANDROID_MODULES_PATH = HOME+'StaticAnalysis/Android/modules'
    SCAN_REPORT_PATH = HOME+'web/media/scans/'
    DECOMPILED_PATH = HOME+'web/media/scans/'
    ANDROGUARD_PATH = HOME+'StaticAnalysis/Android/modules/androguard'
    UNUSED_PERMISSIONS_PATH = HOME+'StaticAnalysis/Android/modules/UnusedPermissions/'
    PLAY_API = HOME + 'StaticAnalysis/Android/play'
    ATS_MODULE = HOME + 'ATS/Server'
    ADB_PATH = ANDROID_SDK_PATH + 'platform-tools/adb'
    AUTOCOMPLETE_PATH = HOME + 'Scraper/googleplay-api/search.py'
    LOG_FILE_NAME = HOME + 'web/media/scans/'
    MITMPROXY_PATH = HOME + 'mitmproxy'
    FABFILE_PATH = HOME + 'web/scanner/fabfile.py'
    MEDIA_APKS = HOME + 'web/media/apks'

After configuring these paths make sure to configure all the path present in config file inside StaticAnalysis directory.

For setting up pdf to work correctly, follow these steps::

    $ apt-get install wkhtmltopdf
    $ apt-get install xvfb
    $ printf '#!/bin/bash\nDISPLAY=localhost:1.0 xvfb-run --auto-servernum --server-num=1 --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf $*' > /usr/bin/wkhtmltopdf.sh
    $ chmod a+x /usr/bin/wkhtmltopdf.sh
    $ ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf
    $ wkhtmltopdf http://www.google.com output.pdf

Note: If the above code won't work, please replace the content of wkhtmltopdf.sh with the content present in the production server.

For running the queue system, use this command::

    $ python manage.py rqworker

You can now run the usual Django ``runserver`` command (replace ``yourapp`` with the name of the directory containing the Django project)::

    $ python web/manage.py runserver

For Booting of emulators, use this code snippet::

    from scanner.docker import *
    automate(n=2), where n is the number of emulators to boot

For Modifying user's balance, use this code snippet::

    from scanner.models import *
    a = UserProfile.objects.get(email="user@email.com")
    a.balance = <amount>
    a.save()

Below is the code snippet for running celery queue which was implemented earlier, but depreceated in current version::

    $ nohup python /home/appwatch/aw-core/web/manage.py celery worker --loglevel=info --concurrency=1 -E </dev/null &

    $ nohup python /home/appwatch/aw-core/web/manage.py celerycam </dev/null &

    $ nohup node /home/appwatch/aw-core/nodejs/myserver.js </dev/null &


