from django.urls import path

from farm_food_project.product.views import ListProductsView, ProductDetailsView, CreateProductView, EditProductView, \
    DeleteProductView

urlpatterns = (
    path('', ListProductsView.as_view(), name='list products'),
    path('details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
    path('create/', CreateProductView.as_view(), name='create product'),
    path('edit/<int:pk>', EditProductView.as_view(), name='edit product'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete product'),
)