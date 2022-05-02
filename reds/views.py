from django.shortcuts import render, get_object_or_404
#かんたんログイン用
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect

#from django.contrib.auth.models import User
#Customized User model
from users.models import User


def home(request):
	return render(request, "home.html")	


#かんたんログイン用
def guest_login(request):
    guest_user = User.objects.get(email='guestuser@gmail.com')
    login(request, guest_user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('home')