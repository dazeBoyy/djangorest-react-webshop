# from django.db.models import Q
# from django.http import Http404
# from django.shortcuts import render
# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.generics import ListAPIView
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
# from libraby_shop.product.models import Product, Category, Author
# from libraby_shop.product.serializer import ProductSerializer, CategorySerializer, AuthorSerializer
#
# # Create your views here.
# class LatestProductsList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()[0:4]
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#
# class ProductDetail(APIView):
#     def get_object(self, category_slug, product_slug):
#         try:
#             return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
#         except Product.DoesNotExist:
#             raise Http404
#     def get(self, request, category_slug, product_slug, format=None):
#         product = self.get_object(category_slug,product_slug)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
# class CategoryDetail(APIView):
#     def get_object(self, category_slug):
#         try:
#             return Category.objects.get(slug=category_slug)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def get(self, request, category_slug, format=None):
#         category = self.get_object(category_slug)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#
# class AuthorDetail(APIView):
#     def get_object(self, name):
#         try:
#             return Author.objects.get(name=name)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def get(self, request, name, format=None):
#         author = self.get_object(name)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data)
#
#
# class ApiSearh(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (SearchFilter, OrderingFilter)
#     search_fields = ('title', 'description', 'author__name', 'category__name')
#
