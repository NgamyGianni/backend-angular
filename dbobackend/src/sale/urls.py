from django.urls import path
from sale import views

urlpatterns = [
    path('sales/', views.SaleList.as_view()),
    path('sale/<int:pk>/', views.Sale.as_view()),
]