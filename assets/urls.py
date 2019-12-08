from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<person_name>/', views.persons, name='persons'),
]
