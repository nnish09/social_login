from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('',views.home,name='home'), 
    path('signup',views.signup,name='signup'),  
    path('base',views.base,name='base'), 
    path('student_base',views.student_base,name='student_base'), 
    path('login_user',views.login_user,name='login_user'), 
    path('dashboard',views.dashboard,name='dashboard'),

    path('password/', views.change_password, name='change_password'),
    path('passwordchanged/', views.change_password_done, name='passwordchanged'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
]