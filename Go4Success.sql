-- ***************************
-- * Standard SQL generation *
-- ***************************


-- Database Section
-- ________________

/* create database django_project; */


-- TableSpace Section
-- __________________

-- Table Section
-- _____________

create table ACTIVITY (
	ACTIVITY_ID INT AUTO_INCREMENT,
	ACTIVITY_TYPE char(255) not null,
	ACTIVITY_NAME char(255) not null,
	DATE_START date not null,
	DATE_END date not null,
	ROOM_NAME char(255) not null,
	ROOM_SITE char(255) not null,
	COURSE_CODE char(9),
	primary key (ACTIVITY_ID));

create table ADMIN (
	ADMIN_ID INT AUTO_INCREMENT,
	primary key (ADMIN_ID));

create table ANNOUNCEMENT (
	ANNOUNCEMENT_ID INT AUTO_INCREMENT,
	TITLE char(255) not null,
	DESCRIPTION text(2048) not null,
	PUB_DATE date not null,
	COURSE_CODE char(1),
	TEACHER_ID INT,
	primary key (ANNOUNCEMENT_ID));

create table ATTENDS (
	ACTIVITY_ID INT,
	STUDENT_ID INT,
	primary key (STUDENT_ID, ACTIVITY_ID));

create table COURSE (
	COURSE_CODE char(1) not null,
	primary key (COURSE_CODE));

create table GIVES (
	ACTIVITY_ID INT not null,
	TEACHER_ID INT not null,
	primary key (TEACHER_ID, ACTIVITY_ID));

create table MESSAGE (
	MESSAGE_ID INT AUTO_INCREMENT,
	CONTENT text(520) not null,
	DATE date not null,
	TO_USER_ID INT not null,
	FROM_USER_ID INT not null,
	primary key (MESSAGE_ID));

create table PROFESSOR (
	TEACHER_ID INT AUTO_INCREMENT,
	primary key (TEACHER_ID));

create table REGISTERED (
	STUDENT_ID INT not null,
	COURSE_CODE char(1) not null,
	primary key (STUDENT_ID, COURSE_CODE));

create table ROOM (
	ROOM_NAME char(255) not null,
	ROOM_SITE char(255) not null,
	primary key (ROOM_NAME, ROOM_SITE));

create table SEES (
	ANNOUNCEMENT_ID INT not null,
	USER_ID INT not null,
	primary key (ANNOUNCEMENT_ID, USER_ID));

create table STUDENT (
	STUDENT_ID INT AUTO_INCREMENT,
	STUDENT_NUMBER char(1),
	NOMA char(1) not null,
	primary key (STUDENT_ID));

create table TEACHER (
	TEACHER_ID INT AUTO_INCREMENT,
	IS_TUTOR int(1),
	IS_PROFESSEUR int(1),
	TUTOR_ID INT,
	primary key (TEACHER_ID));

create table TUTOR (
	TUTOR_ID INT AUTO_INCREMENT,
	primary key (TUTOR_ID));

create table APP_USER (
	USER_ID INT AUTO_INCREMENT,
	E_MAIL text(320) not null,
	USERNAME char(64) not null,
	LAST_NAME char(64) not null,
	FIRST_NAME char(64) not null,
	PASSWORD char(64) not null,
	TEACHER_ID INT,
	STUDENT_ID INT,
	ADMIN_ID INT,
	primary key (USER_ID));


-- Constraints Section
-- ___________________

alter table ACTIVITY add constraint FKIN
	foreign key (ROOM_NAME, ROOM_SITE)
	references ROOM;

alter table ACTIVITY add constraint FKFOR
	foreign key (COURSE_CODE)
	references COURSE;

alter table ADMIN add constraint FKUSE_ADM
	foreign key (ADMIN_ID)
	references APP_USER;

alter table ANNOUNCEMENT add constraint FKIS_RELATED_TO
	foreign key (COURSE_CODE)
	references COURSE;

alter table ANNOUNCEMENT add constraint FKCREATES
	foreign key (TEACHER_ID)
	references TEACHER;

alter table ATTENDS add constraint FKATT_STU
	foreign key (STUDENT_ID)
	references STUDENT;

alter table ATTENDS add constraint FKATT_ACT
	foreign key (ACTIVITY_ID)
	references ACTIVITY;

alter table GIVES add constraint FKGIV_TEA
	foreign key (TEACHER_ID)
	references TEACHER;

alter table GIVES add constraint FKGIV_ACT
	foreign key (ACTIVITY_ID)
	references ACTIVITY;

alter table ACTIVITY add constraint 
	check(exist(select * from GIVES
	            where GIVES.ACTIVITY_ID = ACTIVITY_ID));

alter table MESSAGE add constraint FKTO
	foreign key (TO_USER_ID)
	references APP_USER;

alter table MESSAGE add constraint FKFROM
	foreign key (FROM_USER_ID)
	references APP_USER;

alter table PROFESSOR add constraint FKTEA_PRO
	foreign key (TEACHER_ID)
	references TEACHER;

alter table REGISTERED add constraint FKREG_STU
	foreign key (STUDENT_ID)
	references STUDENT;

alter table REGISTERED add constraint FKREG_COU
	foreign key (COURSE_CODE)
	references COURSE;

alter table SEES add constraint FKSEE_USE
	foreign key (USER_ID)
	references APP_USER;

alter table SEES add constraint FKSEE_ANN
	foreign key (ANNOUNCEMENT_ID)
	references ANNOUNCEMENT;

alter table STUDENT add constraint FKUSE_STU
	foreign key (STUDENT_ID)
	references APP_USER;

alter table TEACHER add constraint EXTONE_TEACHER
	check((PROFESSOR is not null and TUTOR is null)
	      or (PROFESSOR is null and TUTOR is not null));

alter table TEACHER add constraint FKUSE_TEA
	foreign key (TEACHER_ID)
	references APP_USER;

alter table TUTOR add constraint FKTEA_TUT
	foreign key (TUTOR_ID)
	references TEACHER;

alter table GO_4SUCCESS_USER add constraint LSTONE_GO_4SUCCESS_USER
	check(ADMIN is not null or STUDENT is not null or TEACHER is not null);


-- Index Section
-- _____________

create unique index ID_ACTIVITY
	on ACTIVITY(ID);

create index FKIN
	on ACTIVITY (ROOM_NAME, ROOM_SITE);

create index FKFOR
	on ACTIVITY (COURSE_CODE);

create unique index FKUSE_ADM
	on ADMIN(ID);

create unique index ID_ANNOUNCEMENT
	on ANNOUNCEMENT(ID);

create index FKIS_RELATED_TO
	on ANNOUNCEMENT (COURSE_CODE);

create index FKCREATES
	on ANNOUNCEMENT (CREATOR_ID);

create unique index ID_ATTENDS
	on ATTENDS(STUDENT_ID, ACTIVITY_ID);

create index FKATT_ACT
	on ATTENDS (ACTIVITY_ID);

create unique index ID_COURSE
	on COURSE(COURSE_CODE);

create unique index ID_GIVES
	on GIVES(TEACHER_ID, ACTIVITY_ID);

create index FKGIV_ACT
	on GIVES (ACTIVITY_ID);

create unique index ID_MESSAGE
	on MESSAGE(ID);

create index FKTO
	on MESSAGE (TO_ID);

create index FKFROM
	on MESSAGE (FROM_ID);

create unique index FKTEA_PRO
	on PROFESSOR(ID);

create unique index ID_REGISTERED
	on REGISTERED(ID, COURSE_CODE);

create index FKREG_COU
	on REGISTERED (COURSE_CODE);

create unique index ID_ROOM
	on ROOM(SITE, NAME);

create unique index ID_SEES
	on SEES(ANNOUNCEMENT_ID, GO_4SUCCESS_USER_ID);

create index FKSEE_USE
	on SEES (GO_4SUCCESS_USER_ID);

create unique index FKUSE_STU
	on STUDENT(ID);

create unique index FKUSE_TEA
	on TEACHER(ID);

create unique index FKTEA_TUT
	on TUTOR(ID);

create unique index ID_GO_4SUCCESS_USER
	on GO_4SUCCESS_USER(ID);

