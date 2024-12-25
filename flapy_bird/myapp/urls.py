from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ensure you have at least one valid route
]
