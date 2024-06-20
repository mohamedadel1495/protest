from django.urls import path
from .views import *


urlpatterns = [
path('add_costcenter',add_costcenter,name='add_costcenter'),
path('update_costcenter/<int:id>',update_costcenter,name='update_costcenter'),
path('delete_costcenter/<int:id>',delete_costcenter,name='delete_costcenter'),
path('',show_costcenter,name='show_costcenter'),
]
