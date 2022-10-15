from django.urls import path , include

from . import views

app_name = 'albums'
urlpatterns = [
    path('', views.index, name='index')
]