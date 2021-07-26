from django.urls import path, include
from . import views

urlpatterns = [
    path('hey', views.hey),
    path('', views.index),
    path('blog',views.blog),
    path('appointment',views.appointment),

]