from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Event

def get_events_list(request):
	day1 = Event.objects.filter(day_of_event='day1')
	day2 = Event.objects.filter(day_of_event='day2')
	day3 = Event.objects.filter(day_of_event='day3')
	day4 = Event.objects.filter(day_of_event='day4')
	day5 = Event.objects.filter(day_of_event='day5')
	day6 = Event.objects.filter(day_of_event='day6')
	return render_to_response('index.html', {'day1':day1,'day2':day2,'day3':day3,'day4':day4,'day5':day5,'day6':day6})