from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@login_required
def add_products(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render (request, 'add_products.html', {'form': form})

@login_required
def update_products(request, id):
    products = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=products)

    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render (request, 'add_products.html', {'form': form})

@login_required
def delete_products(request, id):
    products = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        products.delete()
        return redirect('list_products')

    return render(request, 'product_delete_confirm.html', {'products': products})