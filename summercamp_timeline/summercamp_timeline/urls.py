"""summercamp_timeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import get_events_list, propose_to_talk, profile, userprofile, pending_admin_approvals

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', get_events_list, name='home'),
    url(r'^propose/$', propose_to_talk, name='propose'),
    url(r'^pending_admin_approvals/$', pending_admin_approvals, name='pending_admin_approvals'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^userprofile/$', userprofile, name='user_profile'),
    url(r'^accounts/', include('allauth.urls')),    
]
