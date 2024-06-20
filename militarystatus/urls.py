from django.urls import path
from .views import *


urlpatterns = [
path('add_militarystatus',add_militarystatus,name='add_militarystatus'),
path('update_militarystatus/<int:id>',update_militarystatus,name='update_militarystatus'),
path('delete_militarystatus/<int:id>',delete_militarystatus,name='delete_militarystatus'),
path('',show_militarystatus,name='show_militarystatus'),
]
