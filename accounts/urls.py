from django.urls import path
from django.contrib import admin
from . import views as accounts_views

urlpatterns = [
    path('', accounts_views.signup, name='signup'),
    #path('')
]