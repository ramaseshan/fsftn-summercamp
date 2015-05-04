# fsftn-summercamp
The timeline app of FSFTN Summercamp 2015

## Technologies/Frameworks Used :

Python 2.7  (python.org)

Django 1.8.1 (djangoproject.com)

Jquery 2.2 (jquery.com)

Materialize (materializecss.com)

## How to Run locally :
1. Install Python Development

	Debian : sudo apt-get install python-dev

	Fedora : sudo dnf install python-devel

2. Install pip and virtualenv.

	Refer This for installation : https://virtualenv.pypa.io/en/latest/

3. Create a virtualenv and activate it

	Above link itself provides the steps for the same

4. Clone this project

	git clone https://github.com/ramaseshan/fsftn-summercamp.git

5. Install the requirements

	cd summercamp_timeline/

	pip install -r requirements.txt

6. Run the server

        chmod +x manage.py

        ./manage.py runserver

	open 127.0.0.1:8000

7. Create a SuperUser

	Run the command ./manage.py createsuperuser
	
	Run the server and go to admin login /admin/

	Choose the users app, and edit the superuser account you just created, and add a First Name called "Needs a Speaker"

	Note : This user should not be used for anyother purpose other than managing. Do not propose for events with this user account. JUST FOR ADMINISTRATIVE PURPOSE

8. Activate Social Account login
     	Refer this and setup, facebook login : http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/


Colur Choices :
Primary colour : deep-orange lighten-2
Secondary Color : Default Materialize Green
