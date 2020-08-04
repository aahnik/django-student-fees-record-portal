from django.contrib import admin
from .models import AcadType, AcadTarget, SessionCode, StudyCenter, Section, Grade, Batch, Student

admin.site.register(AcadType)
admin.site.register(AcadTarget)
admin.site.register(SessionCode)
admin.site.register(StudyCenter)
admin.site.register(Section)
admin.site.register(Grade)
admin.site.register(Batch)
admin.site.register(Student)
