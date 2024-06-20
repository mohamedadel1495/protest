from django.urls import path
from .views import *


urlpatterns = [
path('add_gender',add_gender,name='add_gender'),
path('update_gender/<int:id>',update_gender,name='update_gender'),
path('delete_gender/<int:id>',delete_gender,name='delete_gender'),
path('',show_gender,name='show_gender'),
]
