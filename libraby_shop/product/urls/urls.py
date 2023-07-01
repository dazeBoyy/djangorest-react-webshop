from django.urls import path
from libraby_shop.product.views.views import LatestProductsList, ProductDetail, CategoryDetail, AuthorDetail, ApiSearh

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
    path('products/search/', ApiSearh.as_view(), name='search'),
    path('products/author/<str:name>/', AuthorDetail.as_view(), name='author-detail'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view(), name='category-detail'),


]