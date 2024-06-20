from django.urls import path, re_path
from .views import *
urlpatterns = [
path('register',register_customer,name='register'),
path('login',login_customer,name='login'),
path('logout',logout_customer,name='logout'),
path('',show_users,name='show_users'),
path('delete_user/<int:id>',delete_user,name='delete_user'),
path('add_edit_user_permissions/<int:id>',add_edit_user_permissions,name='add_edit_user_permissions'),
path('add_user',add_user,name='add_user'),
path('add_group',add_group,name='add_group'),
path('group_list/', group_list, name='group_list'),
path('edit_group/<int:id>',edit_group,name='edit_group'),

]
