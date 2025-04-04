from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductCreationForm, CategoryForm, EditProductForm


def get_index_page(request):
    products = Product.objects.all()
    form = ProductCreationForm()
    return render(request, 'index.html', {'products': products, 'form': form})


def get_categories_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        form = CategoryForm()
        return render(request, 'categories.html', {'form': form, 'categories': categories})
    if request.method == 'POST':
        categories = Category.objects.all()
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category(name=form.data.get('name'))
            category.save()
            return redirect(to='categories_list_page')
        else:
            return render(request, 'categories.html', {'form': form, 'categories': categories, 'error': 'SOMETHING WENT WRONG'})



def edit_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'GET':
        form = CategoryForm(data={'name': category.name})
        return render(request, 'edit-category.html', {'form': form, 'category': category})
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category.name = form.data.get('name')
            category.save()
            return redirect(to='categories_list_page')
        else:
            return render(request, 'edit-category.html', {'form': form, 'category': category, 'error': 'SOMETHING WENT WRONG'})


def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect(to='categories_list_page')


def get_category_products(request, pk):
    if request.method == 'GET':
        category = Category.objects.get(id=pk)
        products = Product.objects.filter(category_id=category.id)
        form = ProductCreationForm()
        return render(request, 'category-products.html', {'category': category, 'products': products, 'form': form})
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        category = Category.objects.get(id=pk)
        if form.is_valid():
            name = form.data.get('name')
            quantity = form.data.get('quantity')
            price = form.data.get('price')
            category_id = category.id
            new_product = Product(name=name, quantity=quantity, price=price, category_id=category_id)
            new_product.save()
            return redirect(to='category_product_list', pk=category_id)
        else:
            return render(request, 'category-products.html', {'category': category, 'products': products, 'form': form, 'error': 'ERROR!'})



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
    categories = Category.objects.all()
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        category_id = product.category.id
        form = EditProductForm(data={'name': product.name, 'quantity': product.quantity, 'price': product.price, 'category_id': category_id})
        return render(request, 'edit-product.html', {'form': form, 'product': product, 'categories': categories})
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        form = EditProductForm(request.POST)
        if form.is_valid():
            product.name = form.data.get('name')
            product.price = form.data.get('price')
            product.quantity = form.data.get('quantity')
            product.category_id = form.data.get('category_id')
            product.save()
            return redirect(to='category_product_list', pk=form.data.get('category_id'))
        else:
            return render(request, 'edit-product.html', {'form': form, 'product': product, 'error': 'Something went wrong'})





