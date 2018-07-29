from django.urls import path
# Create your views here.
from . import views

app_name = "products"
urlpatterns = [
    path('', views.index, name='index')
]