from django.contrib import admin
from .models import *

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'date_start', 'date_end', 'in_site', 'in_name', 'course_code')
    search_fields = ('id', 'type', 'name', 'date_start', 'date_end', 'in_site', 'in_name', 'course_code')

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('id', 'user')
    
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'pub_date', 'course_code', 'creator')
    search_fields = ('id', 'title', 'description', 'pub_date', 'course_code', 'creator')
    
class AttendsAdmin(admin.ModelAdmin):
    list_display = ('activity', 'student')
    search_fields = ('activity', 'student')
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code',)
    search_fields = ('course_code',)
    
class GivesAdmin(admin.ModelAdmin):
    list_display = ('activity', 'teacher')
    search_fields = ('activity', 'teacher')
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'date', 'to', 'from_field')
    search_fields = ('id', 'content', 'date', 'to', 'from_field') 
    
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher')
    search_fields = ('id', 'teacher')
    
class RegisteredAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_code')
    search_fields = ('student', 'course_code')
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'site')
    search_fields = ('name', 'site')
    
class SeesAdmin(admin.ModelAdmin):
    list_display = ('user', 'announcement')
    search_fields = ('user', 'announcement')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'noma', 'user')
    search_fields = ('id', 'noma', 'user')
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('id', 'user')
    
class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher')
    search_fields = ('id', 'teacher')
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'e_mail', 'name', 'first_name', "pwd")
    search_fields = ('id', 'e_mail', 'name', 'first_name', 'pwd')
    
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Attends, AttendsAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Gives, GivesAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Registered, RegisteredAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Sees, SeesAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(User, UserAdmin)