hi:
	@cat README.md
	@echo "Press [ENTER] to continue"
	@read consent

dev:
	@echo Setting up dev environment ...
	python3 -m venv venv &&\
	. venv/bin/activate &&\
	pip install -r requirements.txt

migrations:
	@echo Making migrations ...
	. venv/bin/activate;\
	cd cdiig;\
	python3 manage.py makemigrations student_management;\
	python3 manage.py migrate

fill:
	@echo Filling database with some dummy data ...
	. venv/bin/activate;\
	cd cdiig && python3 manage.py shell < fill_dummy.py

super:
	@echo Creating super user ...
	. venv/bin/activate;\
	cd cdiig && python3 manage.py createsuperuser

server:
	@echo Running django development server ...
	. venv/bin/activate;\
	cd cdiig && python3 manage.py runserver

first_time: hi dev migrations fill super server
