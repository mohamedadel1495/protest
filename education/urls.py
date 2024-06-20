from django.urls import path
from .views import *


urlpatterns = [
path('add_education',add_education,name='add_education'),
path('update_education/<int:id>',update_education,name='update_education'),
path('delete_education/<int:id>',delete_education,name='delete_education'),
path('',show_education,name='show_education'),
]
