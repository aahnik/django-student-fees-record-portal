from django.contrib import admin
from .models import AcadType, AcadTarget, FeesRecord, SessionCode, StudyCenter, Section, Grade, Batch, Student
from django.forms import CheckboxSelectMultiple
admin.site.register(AcadType)
admin.site.register(AcadTarget)
admin.site.register(SessionCode)
admin.site.register(StudyCenter)
admin.site.register(Section)
admin.site.register(Grade)
admin.site.register(Batch)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_name', 'batchCode', 'sessionCode')


admin.site.register(Student, StudentAdmin)
admin.site.register(FeesRecord)
