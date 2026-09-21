from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world , name='home'),
    path('brasil/', views.HelloBrazil.as_view(), name='brasil'),
    path('reservation', views.home),
]