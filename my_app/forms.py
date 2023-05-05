from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from .models import *

# SIGNAL_TYPE = [
#     ("01", "Stakeholders Being Hired In Customer Accounts"),
#     ("02", "Stakeholders Leaving Customer Accounts"),
#     ("03", "Customers Moving Into Prospect Accounts"),
#     ("04", "Customers Moving Into Greenfield Accounts"),
#     ("05", "Stakeholders Being Hired In Prospect Accounts"),
#     # ("06", "Competitors Being Hired In Customer Accounts"),
# ]

class SignUpForm(UserCreationForm):
  username = forms.CharField(max_length = 100, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  first_name = forms.CharField(max_length = 30, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  last_name = forms.CharField(max_length = 30, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  email = forms.EmailField(max_length = 224, widget = forms.EmailInput(attrs = {'class': "form-control"}))
  password1 = forms.CharField(max_length = 20, required = True, widget = forms.PasswordInput(attrs = {'class': "form-control"}))
  # password2 = forms.CharField(max_length = 20, required = True, widget = forms.PasswordInput(attrs = {'class': "form-control"}))

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1']

class SignalForm(forms.ModelForm):
  SIGNAL_TYPE_QS = [Q(value=val, label=label) for val, label in SIGNAL_TYPE]
  q = Client.objects.all()
  # signals = []
  # for i in SIGNAL_TYPE:
  #   signals.append(i)
  client = forms.ModelChoiceField(queryset=q, widget=forms.Select(attrs={'class': 'form-control'}))
  signal_type = forms.TypedChoiceField(choices=SIGNAL_TYPE, widget=forms.Select(attrs={'class': 'form-control'}))
  stakeholder_current_company = forms.CharField(max_length = 255, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  stakeholder_first_name = forms.CharField(max_length = 128, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  stakeholder_last_name = forms.CharField(max_length = 128, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  stakeholder_current_title = forms.CharField(max_length = 255, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  stakeholder_time_in_current_role = forms.CharField(max_length = 255, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  stakeholder_current_email = forms.EmailField(max_length = 255, required = True, widget = forms.TextInput(attrs = {'class': "form-control"}))
  class Meta:
    model = Signal
    fields = ['client', 'signal_type','stakeholder_current_company','stakeholder_first_name','stakeholder_last_name', 'stakeholder_current_title','stakeholder_time_in_current_role','stakeholder_current_email']
