'''
Main app urls
'''
from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('program/', views.program, name='program'),
	path('announcements/', views.announcements, name='announcements'),
	path('contacts-resources/', views.contacts_resources, name='contacts-resources'),
  path('<slug:slug>/', views.more, name='more'),
]
