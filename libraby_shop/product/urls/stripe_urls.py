from django.urls import path
from product.views import stripe_views as views


urlpatterns = [
    path('create-checkout-session/',views.create_checkout_session,name="create_checkout_session"),

]
