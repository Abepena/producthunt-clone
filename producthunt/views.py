from django.shortcuts import render
from products.models import Product

def index(request):
    #show a list of products in decending order by upvotes
    products = Product.objects.order_by("-votes_total")
    return render(request, "index.html", {"products":products})