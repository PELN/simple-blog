from django.urls import path

from . import views

app_name = 'blogapp'

urlpatterns = [
    # leave string empty so index is at root
    path('', views.index, name='index'),
    path('details/<int:pk>', views.details, name='details'),
   ]