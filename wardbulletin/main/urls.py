'''
Main app urls
'''
from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('announcements', views.announcements, name='announcements'),
	path('contacts-resources', views.contacts_resources, name='contacts-resources'),
]
