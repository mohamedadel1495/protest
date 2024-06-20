from django.urls import path
from .views import *


urlpatterns = [
path('add_dep',add_dep,name='add_dep'),
path('update_dep/<int:id>',update_dep,name='update_dep'),
path('delete_dep/<int:id>',delete_dep,name='delete_dep'),
path('',show_dep,name='show_dep'),

]
