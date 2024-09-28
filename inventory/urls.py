from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('items/<int:item_id>/', views.ItemDetailView.as_view(), name='item-detail'),
]
