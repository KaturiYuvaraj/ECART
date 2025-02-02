from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from ecartapp.models.customer import Customer
from django.views import  View
from ecartapp.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )