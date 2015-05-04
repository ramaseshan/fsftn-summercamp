from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


from .models import Event , PendingProposals, SpeakerDetails
from .forms import SpeakerDetailsForm

def get_events_list(request):
	day1 = Event.objects.filter(day_of_event='day1').order_by('event_start_time')
	day2 = Event.objects.filter(day_of_event='day2').order_by('event_start_time')
	day3 = Event.objects.filter(day_of_event='day3').order_by('event_start_time')
	day4 = Event.objects.filter(day_of_event='day4').order_by('event_start_time')
	day5 = Event.objects.filter(day_of_event='day5').order_by('event_start_time')
	day6 = Event.objects.filter(day_of_event='day6').order_by('event_start_time')
	return render_to_response('index.html', {'day1':day1,'day2':day2,'day3':day3,'day4':day4,'day5':day5,'day6':day6},context_instance=RequestContext(request))

@login_required
def propose_to_talk(request):
	requested = False
	eventid = request.POST.get('event_id')
	try:
		event = Event.objects.get(event_id=eventid)
	except Exception as e:
		return HttpResponseRedirect("/")
	try:
		PendingProposals.objects.get(event_id=event,user_id=request.user)
		requested = True
	except Exception as e:
		print "Unser not registerd before"
	if not requested:
		try:
			propose = PendingProposals(event_id=event,user_id=request.user)
			propose.save()
		except Exception as e:
			return HttpResponse("An error occured. Can you request your proposal again ?")	
	else:
		return HttpResponseRedirect("/profile/?success=success")	
	return HttpResponseRedirect("/profile/?success=success")

@login_required
def profile(request):
	return_dict = {}
	if request.method == "POST":
		try:
			instance = SpeakerDetails.objects.get(user=request.user)
			form = SpeakerDetailsForm(instance=instance,data=request.POST)
		except Exception as e:
			form = SpeakerDetailsForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.user = request.user
			f.save()
	else:	
		try:
			instance = SpeakerDetails.objects.get(user=request.user)
			form = SpeakerDetailsForm(instance=instance)
		except Exception as e:
			form = SpeakerDetailsForm()
		if request.GET.get('success'):
			return_dict["success"] = request.GET.get('success')
	return_dict["form"] = form
	return render_to_response('profile.html', return_dict,context_instance=RequestContext(request))

def userprofile(request):
	return_dict = {}
	user_id = request.GET.get("speaker")
	user_details = SpeakerDetails.objects.get(id=user_id)
	return_dict["user_profile"] = user_details
	return render_to_response('profile.html', return_dict,context_instance=RequestContext(request))

def pending_admin_approvals(request):
	return_dict = {}
	if request.method == "POST":
		id = request.POST.get("id")
		proposal = PendingProposals.objects.get(id=id)
		event = Event.objects.get(event_name=proposal.event_id)
		speaker = SpeakerDetails.objects.get(user=proposal.user_id)
		event.event_speaker = speaker
		event.save()
		proposal.delete()
		return HttpResponse("Success")	
	else:
		proposals = PendingProposals.objects.all()
		return_dict["proposals"] = proposals

	return render_to_response('proposals.html', return_dict,context_instance=RequestContext(request))	
