from django.urls import path

from . import views
from .views import IntroView


urlpatterns = [
    path('', IntroView.as_view(), name='intro'),
    path('home/', views.home, name='home'),
    path('<int:pk>/read/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
]
