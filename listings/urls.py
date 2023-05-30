from django.urls import path

from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='index'),
    # add more paths here for other views
]
