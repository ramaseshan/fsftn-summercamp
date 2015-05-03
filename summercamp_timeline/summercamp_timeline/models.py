from django.db import models

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
	('certificate','Cirtificate Distribution'),
	('photo','Photo Session'),
	('group','Group Formation'),
	('instructions','Instructions'),
)

class Event(models.Model):
	event_id = models.AutoField(primary_key=True)
	event_name = models.CharField(max_length=200,blank=False,null=False,verbose_name="Name of the Event")
	event_desc = models.TextField()
	event_start_time = models.DateTimeField()
	event_end_time = models.DateTimeField()
	event_speaker = models.CharField(max_length=200,blank=True,null=True,verbose_name="Name of the Speaker")
	event_speaker_qual = models.CharField(max_length=200,blank=True,null=True,verbose_name="Speaker Qualifications (optional)")
	event_type = models.CharField(max_length=12, choices=EVENT_TYPE,default='handson',verbose_name="Type of the Event")
	day_of_event = models.CharField(max_length=4, choices=DAYS_CHOICES,default='day1',verbose_name="Which day of the Camp")

	def __unicode__(self):
		return self.event_name