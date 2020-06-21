from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('account/', views.account_page, name='order'),
    path('apply_food/', views.apply_food, name='apply'),

]