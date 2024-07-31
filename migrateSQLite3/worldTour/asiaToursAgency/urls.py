from django.urls import path
from . import views

# We need to define a list of url patterns here
urlpatterns = [
    path('', views.index, name='index'),
]
