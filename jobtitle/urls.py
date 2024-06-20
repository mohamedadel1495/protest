from django.urls import path
from .views import *


urlpatterns = [
path('add_jobtitle',add_jobtitle,name='add_jobtitle'),
path('update_jobtitle/<int:id>',update_jobtitle,name='update_jobtitle'),
path('delete_jobtitle/<int:id>',delete_jobtitle,name='delete_jobtitle'),
path('',show_jobtitle,name='show_jobtitle'),
]
