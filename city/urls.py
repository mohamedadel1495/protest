from django.urls import path
from .views import *


urlpatterns = [
path('add_city',add_city,name='add_city'),
path('update_city/<int:id>',update_city,name='update_city'),
path('delete_city/<int:id>',delete_city,name='delete_city'),
path('',show_city,name='show_city'),
]
