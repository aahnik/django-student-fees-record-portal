from cdiig.student_management.models import AcadTarget, Batch, Grade, Section, SessionCode, Student, StudyCenter
from django.contrib import admin
from .models import AcadType, AcadTarget, SessionCode,
StudyCenter, Section, Grade, Batch, Student

admin.site.register(AcadType, AcadTarget, SessionCode,
                    StudyCenter, Section, Grade, Batch, Student)
