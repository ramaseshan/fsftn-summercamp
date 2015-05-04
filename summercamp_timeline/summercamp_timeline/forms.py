from django import forms

from .models import SpeakerDetails

class SpeakerDetailsForm(forms.ModelForm):
	class Meta:
		model = SpeakerDetails
		exclude = ['user']

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()