from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('personal_info','job_title','department', 'location','expertise',
        'phone_number','contact_facebook','contact_linkedin','contact_skype')
