from django.db import models

class ROOM(models.Model):
    site_name = models.CharField(db_column='SITE_NAME', primary_key=True, max_length=255)
    room_name = models.CharField(db_column='ROOM_NAME', primary_key=True, max_length=255)
        
class COURSE(models.Model):
    course_code = models.CharField(db_column='COURSE_CODE', primary_key=True, max_length=9)
    
class ACTIVITY(models.Model):
    activity_id = models.AutoField(db_column='ACTIVITY_ID', primary_key=True)
    activity_type = models.CharField(db_column='ACTIVITY_TYPE', max_length=255)
    activity_name = models.CharField(db_column='ACTIVITY_NAME', max_length=255)
    activity_date_start = models.DateField(db_column='ACTIVITY_DATE_START')
    activity_date_end = models.DateField(db_column='ACTIVITY_DATE_END')
    activity_site_name = models.OneToOneField(ROOM, on_delete=models.CASCADE, db_column='ACTIVITY_SITE_NAME', max_length=255)
    activity_room_name = models.OneToOneField(ROOM, on_delete=models.CASCADE, db_column='ACTIVITY_ROOM_NAME', max_length=255)
    activty_course_code = models.OneToOneField(COURSE, on_delete=models.CASCADE, db_column='ACTIVITY_COURSE_CODE', max_length=9, blank=True, null=True)
    
class STUDENT(models.Model):
    student_id = models.AutoField(db_column='STUDENT_ID', primary_key=True)
    noma = models.CharField(db_column='NOMA', max_length=8)
    student_number = models.CharField(db_column='STUDENT_NUMBER', max_length=8, null=True)
    
class ATTENDS(models.Model):
    activity_id = models.OneToOneField(ACTIVITY, on_delete=models.CASCADE, db_column='ACTIVITY_ID', primary_key=True)
    student_id = models.OneToOneField(STUDENT, db_column='STUDENT_ID', primary_key=True, on_delete=models.CASCADE)
    
class TEACHER(models.Model):
    teacher_id = models.AutoField(db_column='TEACHER_ID', primary_key=True)
    is_tutor_or_professeur = models.BooleanField(db_column='IS_TUTOR_OR_PROFESSEUR')
    
class GIVES(models.Model):
    activity_id = models.OneToOneField(ACTIVITY, on_delete=models.CASCADE, db_column='ACTIVITY_ID', primary_key=True)
    teacher_id = models.OneToOneField(TEACHER, db_column='TEACHER_ID', primary_key=True, on_delete=models.CASCADE)

class ANNOUNCEMENT(models.Model):
    announcement_id = models.AutoField(db_column='ANNOUNCEMENT_ID', primary_key=True)
    announcement_title = models.CharField(db_column='ANNOUNCEMENT_TITLE', max_length=255)
    announcement_description = models.TextField(db_column='ANNOUNCEMENT_DESCRIPTION')
    announcement__publication_date = models.DateField(db_column='ANNOUNCEMENT_DATE')
    announcement_course_code = models.OneToOneField(COURSE, on_delete=models.CASCADE, db_column='ANNOUNCEMENT_COURSE_CODE', max_length=9, blank=True, null=True)
    announcement_teacher_id = models.OneToOneField(TEACHER, on_delete=models.CASCADE, db_column='ANNOUNCEMENT_TEACHER_ID')
    
class REGISTERED(models.Model):
    student_id = models.OneToOneField(STUDENT, on_delete=models.CASCADE, db_column='STUDENT_ID', primary_key=True)
    course_code = models.OneToOneField(COURSE, on_delete=models.CASCADE, db_column='COURSE_CODE', primary_key=True)
    
class MESSAGE(models.Model):
    message_id = models.AutoField(db_column='MESSAGE_ID', primary_key=True)
    message_content = models.TextField(db_column='MESSAGE_CONTENT')
    message_date = models.DateField(db_column='MESSAGE_DATE')
    message_to_user_id = models.OneToOneField(STUDENT, on_delete=models.CASCADE, db_column='MESSAGE_TO_USER_ID', max_length=8, blank=True, null=True)
    message_from_user_id = models.OneToOneField(STUDENT, on_delete=models.CASCADE, db_column='MESSAGE_FROM_USER_ID', max_length=8, blank=True, null=True)
  
class APP_USER(models.Model):
    user_id = models.AutoField(db_column='USER_ID', primary_key=True)
    user_email = models.CharField(db_column='USER_EMAIL', max_length=255)
    user_password = models.CharField(db_column='USER_PASSWORD', max_length=255)
    user_first_name = models.CharField(db_column='USER_FIRST_NAME', max_length=255)
    user_last_name = models.CharField(db_column='USER_LAST_NAME', max_length=255)
    is_admin = models.BooleanField(db_column='IS_ADMIN')
    is_teacher = models.BooleanField(db_column='IS_TEACHER')
    is_student = models.BooleanField(db_column='IS_STUDENT')
    
class SEES(models.Model):
    announcement_id = models.OneToOneField(ANNOUNCEMENT, on_delete=models.CASCADE, db_column='ANNOUNCEMENT_ID', primary_key=True)
    user_id = models.OneToOneField(APP_USER, on_delete=models.CASCADE, db_column='USER_ID', primary_key=True)
