from django.urls import path
from .views import *


urlpatterns = [
path('add_region',add_region,name='add_region'),
path('update_region/<int:id>',update_region,name='update_region'),
path('delete_region/<int:id>',delete_region,name='delete_region'),
path('',show_region,name='show_region'),
]
