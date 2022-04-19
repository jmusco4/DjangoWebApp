from django.shortcuts import render
from .models import Products

from .forms import ProductForm

# Create your views here.

def product_detail_view(request):
    obj = Products.objects.get(id=1)
    # context = {'title': obj.title, 'price':obj.price}
    context = {'object':obj}
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    context={}
    if request.method == 'POST':
        print(request.POST['user_name'])
        print(request.POST['email'])
        context = {"name":request.POST['user_name'], 'email':request.POST['email']}
    return render(request, "products/product_create.html", context)

