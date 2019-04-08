from django.contrib.auth.views import LoginView
from django.urls import path,include
from . import views


# namespace
app_name = 'users'

LoginView.template_name='users/login.html'
urlpatterns=[
    # login page
    path('login/',LoginView.as_view() ,name='login'),
    # logout page
    path('logout/', views.logout_view, name='logout'),
    # register page
    path('register/',views.register, name='register'),
]