from django.urls import path
from .views import *


urlpatterns = [
path('add_bank',add_bank,name='add_bank'),
path('update_bank/<int:id>',update_bank,name='update_bank'),
path('delete_bank/<int:id>',delete_bank,name='delete_bank'),
path('',show_bank,name='show_bank'),
]
