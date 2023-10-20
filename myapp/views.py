from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm
from django.shortcuts import render
from .models import Order
from datetime import datetime, timedelta


def base_view(request):
    return render(request, 'base.html')


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_detail.html', {'client': client})


def order_list(request, period):
    if period == '7':
        start_date = datetime.now() - timedelta(days=7)
    elif period == '30':
        start_date = datetime.now() - timedelta(days=30)
    elif period == '365':
        start_date = datetime.now() - timedelta(days=365)
    else:
        start_date = datetime.now() - timedelta(days=365)  # По умолчанию за год

    orders = Order.objects.filter(order_date__gte=start_date)
    return render(request, 'order_list.html', {'orders': orders, 'period': period})


def recent_orders_7(request):
    start_date = datetime.now() - timedelta(days=7)
    orders = Order.objects.filter(order_date__gte=start_date)
    products = set()

    for order in orders:
        products.update(order.products.all())

    return render(request, 'recent_orders.html', {'products': products, 'period': '7'})


def recent_orders_30(request):
    start_date = datetime.now() - timedelta(days=30)
    orders = Order.objects.filter(order_date__gte=start_date)
    products = set()

    for order in orders:
        products.update(order.products.all())

    return render(request, 'recent_orders.html', {'products': products, 'period': '30'})


def recent_orders_365(request):
    start_date = datetime.now() - timedelta(days=365)
    orders = Order.objects.filter(order_date__gte=start_date)
    products = set()

    for order in orders:
        products.update(order.products.all())

    return render(request, 'recent_orders.html', {'products': products, 'period': '365'})


def product_list(request):
    products = Product.objects.all()  # Получаем все товары из базы данных
    return render(request, 'product_list.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def upload_photo(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                'product_list')
    else:
        form = ProductForm()
    return render(request, 'upload_photo.html', {'form': form})
