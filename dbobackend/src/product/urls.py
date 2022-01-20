from django.urls import path
from product import views

urlpatterns = [
    # path('products/', views.RedirectionListeDeProduits.as_view()),
    path('product/<int:pk>/', views.ProductLists.as_view()),
    # path('shipPoints/', views.RedirectionListeDeLivraisons.as_view()),
    # path('shipPoint/<int:pk>/', views.RedirectionDetailLivraison.as_view()),
    # path('onsaleproducts/', views.PromoList.as_view()),
    # path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
    # path('availableproducts/', views.ListProduitsDisponibles.as_view()),
    # path('availableproduct/<int:pk>/', views.ProduitDetailDisponible.as_view()),
]