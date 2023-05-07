from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .decorators import *
from .forms import *
from .utils import *
# Create your views here.

import jwt
import datetime

@unauthenticated_user
def login_view(request):
    if(request.method == 'POST'):
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        messages.error(request,'Username or password is incorrect')
    return render(request, 'login.html')
    # return HttpResponse('<p>hello</p>')

@login_required(login_url='login')
@admin_only
def home_view(request):
   return render(request, 'base.html', {'admin': True})

@login_required(login_url='login')
@admin_only
def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients, 'admin':True})

@login_required(login_url='login')
@admin_only
def signals(request):
    signals = Signal.objects.all()
    return render(request, 'signals.html',{'signals': signals, 'admin':True})

@login_required(login_url='login')
@non_admin
def user_home(request):
    # WORKSPACE_KEY = "137b950f-aafb-4f4b-870f-0069eae14426"
    # WORKSPACE_SECRET = "9620d47acc1092abea9639f9131fd9eecc7019d658247558de9032eb31ed6c4f"
    user = request.user
    client = Client.objects.get(user=user)
    signals = client.signal_set.all()
    # encoded_jwt = jwt.encode(
    #   {"id": client.id,  # Identifier of user or organization.
    #     "name": client.user.username,  # Human-readable name (it will simplify troubleshooting)
    #     "iss": WORKSPACE_KEY,
    #     # "fields": <user fields value>, # (optional) Any user fields you want to attach to your user.
    #     "exp": datetime.datetime.now() + datetime.timedelta(seconds=1440)
    #     }, WORKSPACE_SECRET, algorithm="HS256")
    encoded_jwt = genrerate_token(client)
    return render(request, 'user_home.html',{'admin': False, 'client': client, 'signals': signals, 'access_token': encoded_jwt })

@login_required(login_url='login')
@admin_only
def add_client(request):
   form = SignUpForm()
   if request.method == 'POST':
      username = request.POST.get('username')
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      email = request.POST.get('email')
      password = request.POST.get('password1')
      user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
      user.set_password(password)
      try:
        user.save()
        return redirect("clients")
      except ValueError:
        messages.error(request,'Account with that username already exists. Pick another username')
   return render(request,'add_client.html',{'form': form, 'admin': True})

@login_required(login_url='login')
@admin_only
def add_signal(request):
  form = SignalForm()
  if request.method == 'POST':
    form = SignalForm(request.POST)
    if form.is_valid():
        try:
          form.save()
          signal_data = form.cleaned_data
          client = signal_data.get('client')
          name = signal_data.get("stakeholder_first_name")+" "+signal_data.get("stakeholder_last_name")
          email = signal_data.get('stakeholder_current_email')
          phone = signal_data.get('stakeholder_phone_number')
          company_name = signal_data.get('stakeholder_current_company')
          send_to_i_app(client, name, phone, email, company_name)
          # return render(request, 'signals.html', {'admin': True})
          return redirect("signals")
        except ValueError:
          messages.error(request,'An error occured')
    else:
        messages.error(request,'Enter Correct details. Leave no inputs empty')
  
  return render(request,'add_signal.html',{'form': form, 'admin': True})

def logout_view(request):
   logout(request)
   return redirect('login')
