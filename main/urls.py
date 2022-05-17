from django.urls import path
from . import views

urlpatterns = [
    path('', views.nothing, name="main-root"),
    path('home/', views.home, name="main-home"),
]
