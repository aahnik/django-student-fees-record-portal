source venv_iig_admin/bin/activate
cd cdiig/
python3 manage.py makemigrations student_management
python3 manage.py migrate
python3 manage.py runserver