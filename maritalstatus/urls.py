from django.urls import path
from .views import *


urlpatterns = [
path('add_maritalstatus',add_maritalstatus,name='add_maritalstatus'),
path('update_maritalstatus/<int:id>',update_maritalstatus,name='update_maritalstatus'),
path('delete_maritalstatus/<int:id>',delete_maritalstatus,name='delete_maritalstatus'),
path('',show_maritalstatus,name='show_maritalstatus'),
]
