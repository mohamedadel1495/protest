from django.urls import path
from .views import *
urlpatterns = [
path('add_employee',add_employee,name='add_employee'),
path('update_employee/<int:id>',update_employee,name='update_employee'),
path('delete_employee/<int:id>',delete_employee,name='delete_employee'),
path('',show_employee,name='show_employee'),
    path('ajax/load-sections/', load_sections, name='ajax_load_sections'),

]
