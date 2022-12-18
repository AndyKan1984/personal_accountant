from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/expense/', views.new_expense, name='new expense'),
    path('api/income/', views.new_income, name='new income'),
]
