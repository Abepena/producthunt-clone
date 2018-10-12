from django.urls import path
# Create your views here.
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name='create'),
    path("<int:product_id>", views.detail, name="detail"),
    path("<int:product_id>/upvote>", views.upvote, name="upvote"),
    path("<int:pk>/delete", views.ProductDeleteView.as_view(), name="delete")
]