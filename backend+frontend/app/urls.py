from django.urls import path
from .views import get_outbreak_prediction
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
