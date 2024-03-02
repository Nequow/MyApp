# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    date_start = models.DateField(db_column='DATE_START')  # Field name made lowercase.
    date_end = models.DateField(db_column='DATE_END')  # Field name made lowercase.
    in_site = models.ForeignKey('Room', models.DO_NOTHING, db_column='IN_SITE', to_field="name")  # Field name made lowercase.
    in_name = models.ForeignKey('Room', models.DO_NOTHING, db_column='IN_NAME', related_name='activity_in_name_set')  # Field name made lowercase.
    course_code = models.ForeignKey('Course', models.DO_NOTHING, db_column='COURSE_CODE', to_field="course_code", blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACTIVITY'


class Admin(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN'


class Announcement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION')  # Field name made lowercase.
    pub_date = models.DateField(db_column='PUB_DATE')  # Field name made lowercase.
    course_code = models.ForeignKey('Course', models.DO_NOTHING, db_column='COURSE_CODE', blank=True, null=True)  # Field name made lowercase.
    creator = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='CREATOR_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANNOUNCEMENT'
        


class Attends(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING, db_column='ACTIVITY_ID')  # Field name made lowercase.
    student = models.OneToOneField('Student', models.DO_NOTHING, db_column='STUDENT_ID', primary_key=True)  # Field name made lowercase. The composite primary key (STUDENT_ID, ACTIVITY_ID) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'ATTENDS'
        unique_together = (('student', 'activity'),)


class Course(models.Model):
    course_code = models.CharField(db_column='COURSE_CODE', primary_key=True, max_length=9)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COURSE'


class Gives(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING, db_column='ACTIVITY_ID')  # Field name made lowercase.
    teacher = models.OneToOneField('Teacher', models.DO_NOTHING, db_column='TEACHER_ID', primary_key=True)  # Field name made lowercase. The composite primary key (TEACHER_ID, ACTIVITY_ID) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'GIVES'
        unique_together = (('teacher', 'activity'),)


class Message(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT')  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    to = models.ForeignKey('User', models.DO_NOTHING, db_column='TO_ID')  # Field name made lowercase.
    from_field = models.ForeignKey('User', models.DO_NOTHING, db_column='FROM_ID', related_name='message_from_field_set')  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'MESSAGE'


class Professor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TEACHER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROFESSOR'


class Registered(models.Model):
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='COURSE_CODE')  # Field name made lowercase.
    student = models.OneToOneField('Student', models.DO_NOTHING, db_column='STUDENT_ID', primary_key=True)  # Field name made lowercase. The composite primary key (STUDENT_ID, COURSE_CODE) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'REGISTERED'
        unique_together = (('student', 'course_code'),)


class Room(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, unique=True)  # Field name made lowercase.
    site = models.CharField(db_column='SITE', primary_key=True, max_length=255, unique=True)  # Field name made lowercase. The composite primary key (SITE, NAME) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'ROOM'
        unique_together = (('site', 'name'),)
        
    def __str__(self):
        return self.name + " " + self.site


class Sees(models.Model):
    announcement = models.OneToOneField(Announcement, models.DO_NOTHING, db_column='ANNOUNCEMENT_ID', primary_key=True)  # Field name made lowercase. The composite primary key (ANNOUNCEMENT_ID, USER_ID) found, that is not supported. The first column is selected.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEES'
        unique_together = (('announcement', 'user'),)


class Student(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    noma = models.IntegerField(db_column='NOMA')  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENT'


class Teacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEACHER'


class Tutor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='TEACHER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TUTOR'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=64)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=64)  # Field name made lowercase.
    pwd = models.CharField(db_column='PWD', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER'
