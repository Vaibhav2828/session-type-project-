from django import forms

# class SignUp(forms.Form):
#     first_name = forms.CharField(initial = 'First Name', )
#     last_name = forms.CharField()
#     email = forms.EmailField(help_text = 'write your Email', )
#     Address = forms.CharField(required = False, )
#     Technology = forms.CharField(initial = 'Django', disabled = True, )
#     age = forms.IntegerField()
#     password = forms.CharField(widget = forms.PasswordInput)
#     re_password = forms.CharField(help_text = 'Renter your PASSWORD', widget = forms.PasswordInput)
#
# #Validation - Defing tunction inside class signup
#     def clean_password(self):
#         password = self.cleaned_data['password']
#         if len(password) < 4:
#           raise forms.ValidationError("password is too short")
#         return password


# Validation using Validators
from django.core import validators


class SignUp(forms.Form):
  first_name = forms.CharField(initial = 'First Name', )
  last_name = forms.CharField(required = False)
  email = forms.EmailField(help_text = 'write your email', required = False)
  Address = forms.CharField(required = False, )
  Technology = forms.CharField(initial = 'Django', disabled = True)
  age = forms.IntegerField(required = False, )
  password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
  re_password = forms.CharField(widget = forms.PasswordInput, required = False)

  # Validation - Defing tunction inside class signup
  def clean_password(self):
      password = self.cleaned_data['password']
      if len(password) < 4:
          raise forms.ValidationError("password is too short")
      return password