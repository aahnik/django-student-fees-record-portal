from django.db import models
# LEARNT __str__ must return string


class AcadType(models.Model):
    acad_type = models.CharField('Type', max_length=2)

    def __str__(self):
        return self.acad_type


class AcadTarget(models.Model):
    target_year = models.IntegerField('Target Year')

    def __str__(self):
        return str(self.target_year)


class StudyCenter(models.Model):
    center = models.CharField('Center Location', max_length=20)
    center_id = models.CharField('Center Code', max_length=1, primary_key=True)

    def __str__(self):
        return self.center


class Section(models.Model):  # section/timing in a center
    sec = models.CharField('Section', max_length=1, primary_key=True)

    def __str__(self):
        return self.sec


class Grade(models.Model):
    grade_id = models.CharField('Class Code', max_length=1)
    grade = models.IntegerField('Class')

    def __str__(self):
        return str(self.grade)


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
    acadType = models.ForeignKey(AcadType)
    acadTarget = models.ForeignKey(AcadTarget)
    studyCenter = models.ForeignKey(StudyCenter)
    section = models.ForeignKey(Section)
    grade = models.ForeignKey(Grade)

    feesRecords = models.ManyToManyField(FeesRecord)

    def __str__(self):
        return self.s_name

    def batchCode(self):
        code = self.grade.grade_id+self.studyCenter.center_id+self.section.sec
        return code

    def sessionCode(self):
        code = self.acadType.acad_type+str(self.acadTarget.target_year)
        return code
        