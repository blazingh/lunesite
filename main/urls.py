from django.urls import path
from . import views

urlpatterns = [
    path('', views.nothing, name="ex_list"),
    path('add_ex/', views.add_ex, name="add_ex"),
    path('gen_ex/', views.gen_ex, name="gen_ex"),
]
