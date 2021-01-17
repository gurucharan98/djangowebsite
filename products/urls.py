from django.urls import path, include
from . import views
from .new import newpage

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('my_new/', newpage.new_page)
]