from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.StockListView.as_view(), name='stock_read'),
    path('new/', views.StockCreateView.as_view(), name='new'),
    path('<int:pk>/edit', views.StockUpdateView.as_view(), name='stock_update'),
    
    
    # path('create/', views.create, name="create"),
    # path('', views.product_read, name='product_read'),
    # path('<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.stock_delete, name='stock_delete'),   
]