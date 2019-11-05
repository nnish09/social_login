from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth import login, authenticate,logout,update_session_auth_hash
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from core.models import User
from core.forms import SignUpForm,LoginForm
import json
from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.views import View

user_model = User



def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

@login_required
def student_base(request):
    return render(request, 'student_base.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            user= form.save(commit=False)
            # user.refresh_from_db()  # load the profile instance created by the signal
            user.phone_no = form.cleaned_data.get('phone_no')
            user.save()
           
            return redirect('login_user')  
    else:      
        form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'form': form})






def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)          
            if user is not None:
                if user.is_active:
                    login(request, user)                                                            
                    return redirect('dashboard')                  
    else:
        login_form = LoginForm()
    return render(request, 'registration/login.html', {'login_form': login_form,})




@login_required
def dashboard(request):
    return render(request, 'student_dashboard.html')
   

@login_required
def change_password_done(request):
    return render(request, 'registration/password_changed.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('passwordchanged')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form})