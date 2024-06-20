from django.urls import path
from .views import *


urlpatterns = [
path('add_team',add_team,name='add_team'),
path('update_team/<int:id>',update_team,name='update_team'),
path('delete_team/<int:id>',delete_team,name='delete_team'),
path('',show_team,name='show_team'),
]
