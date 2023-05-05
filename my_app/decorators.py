from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('home')
    else:
      return view_func(request, *args, **kwargs)
  return wrapper_func

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
      print(request.user.username)
      if(request.user.username == "admin"):
        print("verified as admin")
        return view_func(request, *args, **kwargs)
      
      else:
        return redirect('user_home')

      
    return wrapper_func

def non_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
      if(request.user == 'admin'):
        return redirect('home')
      
      else:
        return view_func(request, *args, **kwargs)

      
    return wrapper_func