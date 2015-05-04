from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

DAYS_CHOICES = (
    ('day1', 'Day 1'),
    ('day2', 'Day 2'),
    ('day3', 'Day 3'),
    ('day4', 'Day 4'),
    ('day5', 'Day 5'),
    ('day6', 'Day 6'),
)

EVENT_TYPE = (
	('handson','Hands On'),
	('tea','Tea Break'),
	('lunch','Lunch'),
	('ls','Lightning Talk'),
	('talk','Talks and Discussions'),
	('cultural','Cultural Event'),
	('certificate','Certificate Distribution'),
	('photo','Photo Session'),
	('group','Group Formation'),
	('instructions','Instructions'),
)


class SpeakerDetails(models.Model):
	numeric = RegexValidator(r'^[0-9]*$', message='Only numbers are allowed.')

	user = models.OneToOneField(User)
	mobile_number = models.CharField(unique=True, max_length=20, validators=[numeric],blank=False,null=False)
	facebook = models.CharField(max_length=500,blank=True,null=True)
	twitter = models.CharField(max_length=500,blank=True,null=True)
	diaspora = models.CharField(max_length=500,blank=True,null=True)
	is_mobile_visible = models.BooleanField(default=False,null=False,verbose_name="Make Mobile Number publically visible")
	is_fb_visible = models.BooleanField(default=False,null=False,verbose_name="Make Facebook profile publically visible")
	is_twitter_visible = models.BooleanField(default=False,null=False,verbose_name="Make twitter handle publically visible")
	is_diasp_visible = models.BooleanField(default=False,null=False,verbose_name="Make Diaspora profile publically visible")
	user_desc = models.TextField(verbose_name="Enter Some Description about yourself.",blank=True,null=True)
	user_qual = models.CharField(max_length=500,blank=True,null=True,verbose_name="Your job qualification")

	def __unicode__(self):
		return self.user.first_name

class Event(models.Model):
	event_id = models.AutoField(primary_key=True)
	event_name = models.CharField(max_length=200,blank=False,null=False,verbose_name="Name of the Event")
	event_desc = models.TextField()
	event_start_time = models.DateTimeField()
	event_end_time = models.DateTimeField()
	event_speaker = models.ForeignKey(SpeakerDetails,null=True,blank=True,default="None")
	event_speaker_qual = models.CharField(max_length=200,blank=True,null=True,verbose_name="Speaker Qualifications (optional)")
	event_type = models.CharField(max_length=12, choices=EVENT_TYPE,default='handson',verbose_name="Type of the Event")
	day_of_event = models.CharField(max_length=4, choices=DAYS_CHOICES,default='day1',verbose_name="Which day of the Camp")

	def __unicode__(self):
		return self.event_name


class PendingProposals(models.Model):
	event_id = models.ForeignKey(Event)
	user_id = models.ForeignKey(User)