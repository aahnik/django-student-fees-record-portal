from django.db import models


class AcadType(models.Model):
    acad_type = models.CharField('Academic Session', max_length=2)

    def __str__(self):
        return self.acad_type


class AcadTarget(models.Model):
    target_year = models.IntegerField('Target Year')

    def __str__(self):
        return self.target_year


class SessionCode(models.Model):
    acad_type = models.ForeignKey(AcadType, on_delete=models.CASCADE)
    target_year = models.ForeignKey(AcadTarget, on_delete=models.CASCADE)

    def __str__(self):
        code = self.acad_type+str(self.target_year)
        return code


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
        return self.grade


class Batch(models.Model):
    sessionCode = models.ForeignKey(SessionCode, on_delete=models.CASCADE)
    center = models.ForeignKey(StudyCenter, on_delete=models.CASCADE)
    sec = models.ForeignKey(Section, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class Student(models.Model):
    s_name = models.CharField('Student Name', max_length=25)
    phn_pri = models.CharField('Primary Phone', max_length=10)
    s_email = models.EmailField('Email', null=True, blank=True)
    phn_sec = models.CharField(
        'Other Phone', null=True, max_length=10, blank=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name
