from django.urls import path

from . import views

urlpatterns = [
    path('', views.suggestions, name='suggestions'),
]
