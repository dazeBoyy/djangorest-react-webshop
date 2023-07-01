from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [

        path('admin/', admin.site.urls),
        path('', TemplateView.as_view(template_name='index.html')),
        # path('api/v1/', include('djoser.urls')),
        # path('api/v1/', include('djoser.urls.authtoken')),
        # path('api/v1/', include('product.urls')),
        # path('api/v1/', include('order.urls')),

        path('api/v1/products/', include('product.urls.product_urls')),
        path('api/v1/users/', include('product.urls.user_urls')),
        path('api/v1/orders/', include('product.urls.order_urls')),
        path('api/v1/stripe/', include('product.urls.stripe_urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

