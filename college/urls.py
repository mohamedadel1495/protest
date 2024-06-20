from django.urls import path
from .views import *


urlpatterns = [
path('add_college',add_college,name='add_college'),
path('update_college/<int:id>',update_college,name='update_college'),
path('delete_college/<int:id>',delete_college,name='delete_college'),
path('',show_college,name='show_college'),
]
