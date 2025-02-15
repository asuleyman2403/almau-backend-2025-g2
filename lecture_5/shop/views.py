from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreationForm


def get_index_page(request):
    products = Product.objects.all()
    form = ProductCreationForm()
    return render(request, 'index.html', {'products': products, 'form': form})



def get_products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        form = ProductCreationForm()
        return render(request, 'index.html', {'products': products, 'form': form})
    else:
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            name = form.data.get('name')
            quantity = form.data.get('quantity')
            price = form.data.get('price')
            new_product = Product(name=name, quantity=quantity, price=price)
            new_product.save()
            return redirect(to='index_page')
        else:
            products = Product.objects.all()
            return render(request, 'index.html', {'products': products, 'form': form})


def get_product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product-details.html', {'product': product})


def delete_product_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('/products/')
    except Product.DoesNotExist as e:
        products = Product.objects.all()
        form = ProductCreationForm()
        return render(request, 'index.html', {'products': products, 'form': form, 'error': 'Product does not exist'})


def edit_product(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        form = ProductCreationForm(data={'name': product.name, 'quantity': product.quantity, 'price': product.price})
        return render(request, 'edit-product.html', {'form': form, 'product': product})
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            product.name = form.data.get('name')
            product.price = form.data.get('price')
            product.quantity = form.data.get('quantity')
            product.save()
            return redirect(to='products_list_page')
        else:
            return render(request, 'edit-product.html', {'form': form, 'product': product, 'error': 'Something went wrong'})





