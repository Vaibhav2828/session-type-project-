from django import forms
from mediainstall.models import User_Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = '__all__'
        # field =['fname', 'lname', 'technologies', 'email', 'display_picture']
