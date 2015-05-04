from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


from .models import Event , PendingProposals

def get_events_list(request):
	day1 = Event.objects.filter(day_of_event='day1')
	day2 = Event.objects.filter(day_of_event='day2')
	day3 = Event.objects.filter(day_of_event='day3')
	day4 = Event.objects.filter(day_of_event='day4')
	day5 = Event.objects.filter(day_of_event='day5')
	day6 = Event.objects.filter(day_of_event='day6')
	return render_to_response('index.html', {'day1':day1,'day2':day2,'day3':day3,'day4':day4,'day5':day5,'day6':day6},context_instance=RequestContext(request))

@login_required
def propose_to_talk(request):
	eventid = request.POST.get('event_id')
	event = Event.objects.get(event_id=eventid)
	if not PendingProposals.objects.get(event_id=event,user_id=request.user):
		propose = PendingProposals(event_id=event,user_id=request.user)
		propose.save()
	else:
		return HttpResponse("You have already registered. Approval Pending")	
	return HttpResponse("Thank you for your interest.Pending Approval from one of the organizers.")