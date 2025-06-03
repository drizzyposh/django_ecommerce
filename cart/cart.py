# cart/cart.py
from store.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 1}
        else:
            self.cart[product_id]["quantity"] += 1
        self.session.modified = True

    def total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total = 0
        for key, item in self.cart.items():
            key = int(key)
            quantity = item["quantity"] 
            for product in products:
                if product.id == key:
                    total += product.price * quantity
        return total

            

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_products(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)
    
    def delete(self, product):
        {'4':3, '2':1}
        product_id = str(product)
        # delete from cart
        if product_id in self.cart:
            del self.cart[product_id]

            self.session.modified = True
