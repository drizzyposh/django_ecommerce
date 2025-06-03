from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from  django.http import JsonResponse



# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    products = cart.get_products()
    totals = cart.total()
    return render(request, "cart_summary.html", {"cart_products": products, "totals": totals })


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product = Product.objects.get(id=product_id)
        cart.add(product)
        return JsonResponse({"qty": len(cart)})


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        # call delete func
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        return response
