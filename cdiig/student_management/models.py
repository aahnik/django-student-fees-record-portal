from django.db import models
# LEARNT __str__ must return string

# THIS IS ONLY FOR CD_IIG ADMIN AND ONLY FOR YEAR 2020-21

AcadType_CHOICES = [
    ('MP', 'Madhyamik'),
    ('HS', 'Higher Secondary')
]
AcadTarget_CHOICES = [
    ('21', '2021'),
    ('22', '2022'),
    ('23', '2023')
]

StudyCenter_CHOICES = [
    ('O', 'Bari Shalbagan'),
    ('M', 'Madhyamgram'),
    ('B', 'Bagbazar'),
    ('R', 'Station'),
    ('C','Champadali'),
    ('K','Kailashnagar'),
    ('S','Sodepur'),
    ('-','Not Assigned')
]


Section_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('-', 'Not Assigned')
]


Grade_CHOICES = [
    ('H', '8'),
    ('M', '9'),
    ('R', '10'),
    ('B', '11'),
    ('S', '12')
]


class FeesRecord(models.Model):

    month = models.CharField('Month', max_length=12)

    def __str__(self):
        return self.month


class Student(models.Model):
    s_name = models.CharField('Student Name', max_length=25)
    phn_pri = models.CharField('Primary Phone', max_length=10)
    s_email = models.EmailField('Email', null=True, blank=True)
    phn_sec = models.CharField(
        'Other Phone', null=True, max_length=10, blank=True)

    acadType = models.CharField(max_length=2, choices=AcadType_CHOICES)
    acadTarget = models.CharField(max_length=2, choices=AcadTarget_CHOICES)
    studyCenter = models.CharField(max_length=2, choices=StudyCenter_CHOICES)
    section = models.CharField(max_length=1, choices=Section_CHOICES)
    grade = models.CharField(max_length=2, choices=Grade_CHOICES)

    feesRecords = models.ManyToManyField(FeesRecord, blank=True)

    def __str__(self):
        return self.s_name

    
    def batchCode(self):
        code = self.grade+self.studyCenter+self.section
        return code

    
    def sessionCode(self):
        code = self.acadType+self.acadTarget
        return code

    def active(self):
        pass
    batchCode.admin_order_field = 'grade'
    sessionCode.admin_order_field = 'acadTarget'
