from django.urls import path
from product.views import user_views as views


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('',views.getUsers,name="users"),
    path('register/', views.registerUser, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/',views.getUserProfile,name="user_profile"),
    path('profile/update/',views.updateUserProfile,name="user_profile_update"),
    path('<str:pk>/',views.getUserById,name="get_user"),
    path('update/<str:pk>/',views.updateUser,name="updateUser"),
    path('delete/<str:pk>/',views.deleteUser,name="deleteUser"),

]
