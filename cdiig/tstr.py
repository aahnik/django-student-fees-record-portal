# this script must be run from django shell
# python3 manage.py shell < tstr.py

from student_management.models import Student
print(Student.objects.all())
print("hola")
