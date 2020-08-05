from django.contrib import admin
from .models import FeesRecord, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_name', 'batchCode', 'sessionCode')
    list_filter = ['grade', 'studyCenter', 'section']
    search_fields = ['s_name']


class StudentInLine(admin.TabularInline):
    model = Student.feesRecords.through


@admin.register(FeesRecord)
class FeesRecordAdmin(admin.ModelAdmin):
    model = FeesRecord
    inlines = [StudentInLine]
