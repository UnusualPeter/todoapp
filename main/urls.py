from django.urls import path

from main import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo', views.add_todo, name='add_todo'),
]
