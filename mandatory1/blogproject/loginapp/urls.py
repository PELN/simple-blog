from django.urls import path

from . import views

app_name = 'loginapp'

urlpatterns = [
    # leave string empty so index is at root
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', views.password_reset, name='password_reset'),
   ]