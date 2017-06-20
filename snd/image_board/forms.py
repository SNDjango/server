from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):

    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')



class ProfileForm(forms.ModelForm):

    personal_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    job_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    department = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    expertise = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Format: "+123456". Between 5 and 15 digits allowed.'}))
    contact_facebook = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'form-control'}))
    contact_linkedin = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'form-control'}))
    contact_skype = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'form-control'}))

    class Meta:
        model = Profile
        fields = ('personal_info','job_title','department', 'location','expertise',
        'phone_number','contact_facebook','contact_linkedin','contact_skype')
