from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def index(request):
    return redirect("index")


@login_required(login_url="accounts/login")
def create(request):
    if request.method == "POST":
        print(request.POST.items())
        if (
            request.POST["title"]
            and request.POST["body"]
            and request.FILES["icon"]
            and request.FILES["image"]
        ):
            product = Product()
            product.title = request.POST["title"]
            product.url = request.POST["url"]
            product.body = request.POST["body"]
            product.icon = request.FILES["icon"]
            product.image = request.FILES["image"]
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            # save the instance of the model to the database
            product.save()
            return redirect("index")

        else:
            return render(
                request, "products/create", {"error": "All fields are required"}
            )

    else:
        return render(request, "products/create.html")

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html",{"product": product})

@login_required(redirect_field_name="accounts:login")
def upvote(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect("products:detail", product_id)