from django.urls import path
from . import views
from homepage.views import index
urlpatterns = [
    path('', views.index, name="index"),
    path('symptom_analysis', views.symptom_analysis, name="symptom_analysis"),
    path('result', views.result, name="result"),
]
