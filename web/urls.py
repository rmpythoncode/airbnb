from django.urls import path
from . import views


urlpatterns = [
    path('', views.rooms),
    # path('home', views.home),
]
