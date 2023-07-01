import stripe
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



stripe.api_key = 'sk_test_51NIBhsLu1cuMW26fLp3HeBFFiW7pz9Bpc1Vb5XXfwrYQtQLISbvPqTnH8up6kpHkgE6dVncBDwf5jQQ9Xjs7dDyn00PI4zrHDZ'


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_checkout_session(request):
    data = request.data


    try:
        url = 'http://localhost:3000'
        cartItems = data['cartItems']
        line_items = []

        for item in cartItems:
            product_id = item['product']
            name = item['name']
            image = item['image']
            price = float(item['price'])
            count_in_stock = item['countInStock']
            quantity = item['qty']

            line_item = {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': str(name),
                        'images': [url + str(image)],
                        'metadata': {
                            'id': int(product_id)
                        }
                    },
                    'unit_amount': int(price * quantity),
                },
                'quantity': int(quantity),
            }

            line_items.append(line_item)
        checkout_session = stripe.checkout.Session.create(
            line_items= line_items,
            mode='payment',
            success_url= 'http://localhost:3000/success/',
            cancel_url= 'http://localhost:3000/',
        )
        return Response(checkout_session.url)
    except Exception as e:
        return Response({'msg': 'something went wrong while creating stripe session', 'error': str(e)}, status=500)

