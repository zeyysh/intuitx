# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.conf.urls import url
from users import views
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken import views as authviews

urlpatterns = [
    # Matches any html file 
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    #path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path("logout/", LogoutView.as_view(), name="logout"),
    url(r'^api-token-auth/', authviews.obtain_auth_token),

]
