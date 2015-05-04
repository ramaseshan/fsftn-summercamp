from django.forms import ModelForm

from .models import SpeakerDetails

class SpeakerDetailsForm(ModelForm):
	class Meta:
		model = SpeakerDetails
		exclude = ['user']