# to be run from django shell
# python3 manage.py shell < fillStudentsSCRIPT.py

import csv

from student_management.models import Student

paths = ['sample_data.csv']

for path in paths:
    with open(path, 'r') as file:
        dataDict = csv.DictReader(file)
        for data in dataDict:
            s_name = data['fullNAME']
            phn_pri = data['PHONE']
            grade = data['CLASS']
            batchCode = data[f'batchCodeClass{grade}']
            g = int(grade)
            acadType = 'MP' if g <= 10 else 'HS'
            acadTarget = '21' if (g == 10 or g == 12) else (
                '22' if (g == 9 or g == 11) else '23')
            phn_sec = data['PHONE2']
            email = data['EMAIL']
            std = Student(s_name=s_name.upper(),
                          phn_pri=phn_pri,
                          acadType=acadType,
                          acadTarget=acadTarget,
                          grade=batchCode[0],
                          studyCenter=batchCode[1] if g != 11 else '-',
                          section=batchCode[2] if g != 11 else '-',
                          phn_sec=phn_sec,
                          s_email=email
                          )
            std.save()
