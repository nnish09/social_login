from django import forms
from core.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=254)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254,required=True)
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_no', 'email','password1', 'password2',)
        

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     # username = self.cleaned_data.get('username')
    #     if email and User.objects.filter(email=email).count() > 0:
    #         raise forms.ValidationError('This email address is already registered.')
    #     return email

    # def clean_phone_no(self):
    #     phone_no = self.cleaned_data.get('phone_no')
    #     # username = self.cleaned_data.get('username')
    #     if phone_no and User.objects.filter(phone_no=phone_no).count() > 0:
    #         raise forms.ValidationError('This phone number is already registered.')
    #     return phone_no








class LoginForm(forms.ModelForm):
    username=forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput,max_length=30, required=False)
  
   
    class Meta:
        model = User
        fields = ('username', 'password')

