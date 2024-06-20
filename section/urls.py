from django.urls import path
from .views import *


urlpatterns = [
path('add_section',add_section,name='add_section'),
path('update_section/<int:id>',update_section,name='update_section'),
path('delete_section/<int:id>',delete_section,name='delete_section'),
path('',show_section,name='show_section'),
]
