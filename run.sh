# this is for my local dev environment not for server side
source venv_iig_admin/bin/activate
cd cdiig/
python3 manage.py makemigrations student_management
python3 manage.py migrate
# python3 manage.py shell < fillStudentsSCRIPT.py
# python3 manage.py createsuperuser
python3 manage.py runserver 192.168.1.8:8080