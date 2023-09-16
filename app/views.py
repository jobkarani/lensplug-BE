from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist


# Create your views here

@api_view(['GET'])
def get_user(request, user_id):
    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def generate_cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        request.session.create()
        cart_id = request.session.session_key

    # Serialize the cart identifier
    serializer = CartIdentifierSerializer({'cart_id': cart_id})

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = None
    is_cart_item_exists = False
    cart_item = None

    if request.user.is_authenticated and request.user.id:
        try:
            cart = Cart.objects.get(user=request.user, cart_id=generate_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user, cart_id=generate_cart_id(request))
            cart.save()

        is_cart_item_exists = CartItem.objects.filter(user=request.user, product=product, cart=cart).exists()

    if not is_cart_item_exists:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
            user=request.user,
        )
        cart_item.save()

    # Serialize the created or updated cart item
    cart_item_serializer = CartItemSerializer(cart_item)

    # You can return a JSON response with the serialized cart item
    return Response({'message': 'Cart item added/updated successfully', 'cart_item': cart_item_serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_cart(request, product_id, cart_item_id):
    cart = Cart.objects.get(user=request.user, cart_id=generate_cart_id(request))
    product = get_object_or_404(Product, id=product_id)

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    # Serialize the updated cart item
    cart_item_serializer = CartItemSerializer(cart_item)

    # You can return a JSON response with the serialized cart item
    return Response({'message': 'Cart item updated successfully', 'cart_item': cart_item_serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_cart_item(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=generate_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.filter(id=cart_item_id)

    # Assuming cart_item is a queryset, not an individual object, we should get the first one.
    if cart_item.exists():
        cart_item = cart_item.first()
        cart_item.delete()

    # Serialize the removed cart item
    cart_item_serializer = CartItemSerializer(cart_item)

    # You can return a JSON response with the serialized cart item
    return Response({'message': 'Cart item removed successfully', 'cart_item': cart_item_serializer.data})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart(request): 
    total = 0
    quantity = 0
    sub_total = 0
    grand_total = 0
    cart_items = None
    products = None

    if request.user.is_authenticated and request.user.id:
        try:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
            products = Product.objects.filter(is_available=True)
            
            for cart_item in cart_items:
                total += (cart_item.product.new_price * cart_item.quantity)
                quantity += cart_item.quantity
                sub_total = total
        except ObjectDoesNotExist:
            pass

    else:
        cart = Cart.objects.get(cart_id=generate_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        products = Product.objects.filter(is_available=True)

    for cart_item in cart_items:
        grand_total += (cart_item.product.new_price * cart_item.quantity)

    cart_count = cart_items.count()

    # Serialize cart items and products
    cart_item_serializer = CartItemSerializer(cart_items, many=True)
    product_serializer = ProductSerializer(products, many=True)

    response_data = {
        'total': total,
        'quantity': quantity,
        'sub_total': sub_total,
        'grand_total': grand_total,
        'cart_count': cart_count,
        'cart_items': cart_item_serializer.data,
        'products': product_serializer.data,
    }

    return Response(response_data)