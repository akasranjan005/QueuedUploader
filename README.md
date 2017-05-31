# QueuedUploader
This web app can be used wherever there is a requirement of uploading multiple files. This app uses redis rq for queueing the files to be uploaded and smoothly takes care if all the files have been uploaded.

Documentation:

## 1. This project contains 3 apps
    andro(for androguard)
    django_rq(for redis queue)
    home(for home/index page)

## 2. to up and run this project:
	
As this project has been built on ubuntu, so a flavour of linux will be required or webserver can do.
we will need 2 terminal to fully run this project
change the location to the working directory, i.e. where the project is kept,
then type the following commands
    
    python manage.py migate
    python manage.py makemigartions
    python manage.py syncdb
    python manage.py runserver
		
## On the other Terminal type:

    python manage.py rqworker default

## Now we are ready to Run the project
	
    Open a browser and type
    127.0.0.1:8000/home/

This will take the user to the apk uploading page, where multiple files can be uploaded, and the uploaded file are then moved into the redis queue.

The whole process of queue being executed can be seen in the terminal which was started using rqworker default command.

To see the apk permissions type in browser
 
    127.0.0.1:8000/viewPermission/
