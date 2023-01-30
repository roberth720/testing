from django.shortcuts import render
from . models import Customer, BannerProduct, Product, Cart, Cartitems
from django.http import JsonResponse
import json

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}
    banner = BannerProduct.objects.all()
    products = Product.objects.all()
    return render (request, 'store.html', {'products': products, 'cart': cart, 'banner': banner})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}


    return render(request, 'cart.html', {'cartitems' : cartitems, 'cart':cart})


def checkout(request):
    return render(request, 'checkout.html', {})

def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
    cartitem, created = Cartitems.objects.get_or_create(cart = cart, product = product)

    if action == "add":
        cartitem.quantity += 1
        cartitem.save()
    

    return JsonResponse("Cart Updated", safe = False)


def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = Cartitems.objects.filter(product__name = quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Quantity updated", safe = False)

def productinfo(request, product_id):
    product_info = Product.objects.get(id=product_id)
    return render(request, 'productinfo.html', {'product_info':product_info})

def search(request):
    search_perfume = Product.objects.filter(name__icontains = request.POST.get('name_of_perfume'))
    return render (request, 'search.html', {'search_perfume': search_perfume})