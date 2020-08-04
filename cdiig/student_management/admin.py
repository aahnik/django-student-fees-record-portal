from django.contrib import admin
from .models import AcadType, AcadTarget, FeesRecord, Month, SessionCode, StudyCenter, Section, Grade, Batch, Student

admin.site.register(AcadType)
admin.site.register(AcadTarget)
admin.site.register(SessionCode)
admin.site.register(StudyCenter)
admin.site.register(Section)
admin.site.register(Grade)
admin.site.register(Batch)
admin.site.register(Month)

class FeesInLine(admin.TabularInline):
    model = FeesRecord
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    inlines = [FeesInLine]
    list_display = ('s_name', 'batch')


admin.site.register(Student,StudentAdmin)
