from django.urls import path
from .views import get_outbreak_prediction

urlpatterns = [
    path('predict_outbreak/', get_outbreak_prediction, name='predict_outbreak'),
]
