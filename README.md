# djangorest-react-webshop
# Запуск back-end:
Создание виртуального окружения 
python -m venv tutorial-env
Активация:
tutorial-env\Scripts\activate.bat
Запуск проекта
cd libraby_shop
python manage.py makemigration 
python manage.py migrate
python manage.py runserver
# Запуск front-end:
npm start

В frontend-части была проделана следующая работа:	
 ![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/f38df714-aeed-4c21-83fc-07cb04b702df)
# Рисунок 1.  Страница регистрации.
![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/16b95f92-d01f-412c-b9e6-bbc550cf1925)
# Рисунок 2.  Страница авторизации.

 ![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/87dd23a3-a761-4e05-9ded-4e5f5eb4fe1e)
# Рисунок 3.  Главное меню.
![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/5ecf38c5-3fa3-4ec7-997d-1c50a7c22f8f)

# Рисунок 4. Продукты и пагинация.

![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/5d6b868a-167f-4486-be7a-1ad9b40da60d)

	 
# Рисунок 5. Страница корзины.
 ![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/fb32421f-e12a-4618-8423-3e3158af9575)

# Рисунок 6. Страница продукта.
 ![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/67980266-d89b-4dee-adbd-d6f5857df051)

# Рисунок 7. Страница ввода данных для доставки.
 
![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/99853638-f186-474f-9be8-0b60554c5643)

# Рисунок 8. Страница выбора способа оплаты.	
 ![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/7c999d97-66e0-4734-9d6f-3d0e5cac075c)

# Рисунок 9. Страница оформления.
![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/61e924c6-9200-4ade-a611-fc61c2cfca32)

# Рисунок 10. Страница оплаты через внешний сервис Stripe.
 
![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/fe62d377-25ee-40b7-a726-0bcb34289639)

# Рисунок 11. Страница профиля пользователя.
 ![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/75e3be2f-249d-4cd4-b004-fc1028f024b8)

# Рисунок 12. Админ панель с пользователями.
![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/7071c2b8-9dc4-4e76-98aa-5b43febc35b1)

 
# Рисунок 13. Админ панель с продуктами.
 ![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/7934ca5e-c6ae-4ebf-ba2c-2d3a408a730f)

# Рисунок 14. Админ панель с заказами.

![image](https://github.com/dazeBoyy/djangorest-react-webshop/assets/66539510/8dc8a15f-04a9-45ba-ae97-46de5a326158)
# Рисунок 15. Админ панель с созданием продуктов.

 # END-POINTS:
1.	Получение списка пользователей:
path('',views.getUsers,name="users")
2.	Регистрация нового пользователя:
path('register/', views.registerUser, name='register')
3.	Аутентификация и получение токена доступа:
path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair')
4.	Обновление токена доступа:
path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
5.	Получение профиля пользователя:
path('profile/',views.getUserProfile,name="user_profile")
6.	Обновление профиля пользователя:
path('profile/update/',views.updateUserProfile,name="user_profile_update")
7.	Получение информации о пользователе по идентификатору:
path('<str:pk>/',views.getUserById,name="get_user")
8.	Обновление информации о пользователе по идентификатору:
path('update/<str:pk>/',views.updateUser,name="updateUser")
9.	Удаление пользователя по идентификатору:
path('delete/<str:pk>/',views.deleteUser,name="deleteUser")
10.	Создание сессии оформления заказа:
path('create-checkout-session/',views.create_checkout_session,name="create_checkout_session")
11.	Получение списка продуктов:
path('',views.getProducts,name="products")
12.	Создание нового продукта:
path('create/',views.createProduct,name="create_product")
13.	Загрузка изображения продукта:
path('upload/',views.uploadImage,name="upload_image")
14.	Создание отзыва о продукте:
path('<str:pk>/reviews/',views.createProductReview,name="create-review")
15.	Получение списка лучших продуктов:
path('top/',views.getTopProducts,name="top-products")
16.	Получение информации о продукте по идентификатору:
path('<str:pk>/',views.getProduct,name="product")
17.	Обновление информации о продукте по идентификатору:
path('update/<str:pk>/',views.updateProduct,name="update_product")
18.	Удаление продукта по идентификатору:
path('delete/<str:pk>/',views.deleteProduct,name="delete_product")
19.	Получение списка заказов:
path('',views.getOrders,name="allorders")
20.	Добавление товаров в заказ:
path('add/',views.addOrderItems,name="orders-add")
21.	Получение списка собственных заказов пользователя:
path('myorders/',views.getMyOrders,name="myorders")
22.	Обновление статуса доставки заказа по идентификатору:
path('<str:pk>/deliver/',views.updateOrderToDelivered,name="delivered")
23.	Получение информации о заказе по идентификатору:
path('<str:pk>/',views.getOrderById,name="user-order")
24.	Обновление статуса оплаты заказа по идентификатору:
path('<str:pk>/pay/',views.updateOrderToPaid,name="pay")
