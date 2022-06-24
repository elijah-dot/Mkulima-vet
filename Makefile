serve:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

tests:
	python3 manage.py test

static:
	python3 manage.py collectstatic

super:
	python3 manage.py createsuperuser

shell:
	Python3 manage.py shell

check: 
	python3 manage.py check 

heroku: 
	heroku run python3 manage.py migrate

heroku:
	heroku create

push: 
	git push heroku master