from django.contrib import admin
from .models import FeesRecord, Student


def clearSelectedMonths(modeladmin, request, queryset):
    selectedMonthObjs = [
        month for month in FeesRecord.objects.all() if month.is_selected]

    for mo in selectedMonthObjs:

        for obj in queryset:
            if mo not in obj.feesRecords.all():
                obj.feesRecords.add(mo)


clearSelectedMonths.short_description = "Clear Fees for Selected Students for Months Selected"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_name', 'cleared', 'batchCode', 'sessionCode')
    list_filter = ['grade', 'studyCenter', 'section']
    search_fields = ['s_name']
    actions = [clearSelectedMonths]


# class StudentInLine(admin.TabularInline):
#     model = Student.feesRecords.through


def unselectMonths(modeladmin, request, queryset):
    queryset.update(is_selected=False)


unselectMonths.short_description = "Mark selected Months as Unselected for Action"


def selectMonths(modeladmin, request, queryset):
    queryset.update(is_selected=True)


selectMonths.short_description = "Mark selected Months as Selected for Action"


@admin.register(FeesRecord)
class FeesRecordAdmin(admin.ModelAdmin):
    list_display = ('month', 'is_selected')
    model = FeesRecord
    # inlines = [StudentInLine]
    actions = [unselectMonths, selectMonths]
