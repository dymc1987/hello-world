from django.urls import path

from . import views

app_name = 'assets'
urlpatterns = [
    path('', views.index, name='index'),
    path('<person_name>/', views.assets, name='assets'),
    path('add', views.add, name='add'),
]
