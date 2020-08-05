# to be run from django shell
# python3 manage.py shell < fillStudentsSCRIPT.py

import csv

from student_management.models import Student

load_from_absolute_file_path = '/home/aahnik/Downloads/stdentData.csv'

with open(load_from_absolute_file_path, 'r') as file:
    dataDict = csv.DictReader(file)
    for data in dataDict:
        s_name = data['fullNAME']
        phn_pri = data['PHONE']
        grade = data['CLASS']
        batchCode = data[f'batchCodeClass{grade}']
        g = int(grade)
        acadType = 'MP' if g <= 10 else 'HS'
        acadTarget = '21' if g == (10 or 12) else (
            '22' if g == (9 or 11) else '23')
        phn_sec = data['PHONE2']
        email = data['EMAIL']
        std = Student(s_name=s_name,
                      phn_pri=phn_pri,
                      acadType=acadType,
                      acadTarget=acadTarget,
                      grade=batchCode[0],
                      studyCenter=batchCode[1],
                      section=batchCode[2],
                      phn_sec=phn_sec,
                      s_email=email
                      )
        std.save()
