from django.urls import path
from . import views

urlpatterns = [
   path('', views.page, name='home'),
   path('weather',views.weather,name='weather')
   # path('search', views.result, name='search'),

]
