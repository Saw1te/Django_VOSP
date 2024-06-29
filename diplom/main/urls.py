from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('result', views.result),
    path('step2', views.step2),
    path('step3', views.step3)
]
