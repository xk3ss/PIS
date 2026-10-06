from django.contrib import admin
from .models import Subject, LessonType, Teacher, Group, Lesson


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(LessonType)
class LessonTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'phone', 'experience')
    filter_horizontal = ('subjects',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'department', 'students_count')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'group', 'subject', 'lesson_type',
                    'hours', 'rate_per_hour', 'get_total_payment', 'created_date')