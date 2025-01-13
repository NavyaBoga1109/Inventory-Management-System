from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, Product, SaleOrder
from .forms import SupplierForm, ProductForm, SaleOrderForm

from django.db.models import Q

def index(request):
    category = request.GET.get('category')
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/index.html', {
        'suppliers': suppliers,
        'products': products,
        'categories': Product.objects.values_list('category', flat=True).distinct()
    })

# Supplier CRUD
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SupplierForm()
    return render(request, 'inventory/supplier_form.html', {'form': form})

def edit_supplier(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/supplier_form.html', {'form': form})

def delete_supplier(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    supplier.delete()
    return redirect('index')

# Product CRUD
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('index')

# Sale Order CRUD
def list_sale_orders(request):
    status = request.GET.get('status')
    if status:
        sale_orders = SaleOrder.objects.filter(status=status)
    else:
        sale_orders = SaleOrder.objects.all()
    
    statuses = SaleOrder.objects.values_list('status', flat=True).distinct()
    return render(request, 'inventory/sale_order_list.html', {
        'sale_orders': sale_orders,
        'statuses': statuses
    })

def create_sale_order(request):
    if request.method == 'POST':
        form = SaleOrderForm(request.POST)
        if form.is_valid():
            sale_order = form.save(commit=False)
            sale_order.total_price = sale_order.product.price * sale_order.quantity
            if sale_order.quantity > sale_order.product.stock_quantity:
                return render(request, 'inventory/sale_order_form.html', {
                    'form': form,
                    'error': 'Insufficient stock for this product.',
                })
            sale_order.product.stock_quantity -= sale_order.quantity
            sale_order.product.save()
            sale_order.save()
            return redirect('list_sale_orders')
    else:
        form = SaleOrderForm()
    return render(request, 'inventory/sale_order_form.html', {'form': form})

def edit_sale_order(request, id):
    sale_order = get_object_or_404(SaleOrder, id=id)
    if request.method == 'POST':
        form = SaleOrderForm(request.POST, instance=sale_order)
        if form.is_valid():
            form.save()
            return redirect('list_sale_orders')
    else:
        form = SaleOrderForm(instance=sale_order)
    return render(request, 'inventory/sale_order_form.html', {'form': form})

def delete_sale_order(request, id):
    sale_order = get_object_or_404(SaleOrder, id=id)
    sale_order.product.stock_quantity += sale_order.quantity
    sale_order.product.save()
    sale_order.delete()
    return redirect('list_sale_orders')

def cancel_sale_order(request, id):
    sale_order = get_object_or_404(SaleOrder, id=id)
    if sale_order.status == 'Pending':
        sale_order.product.stock_quantity += sale_order.quantity
        sale_order.product.save()
        sale_order.status = 'Cancelled'
        sale_order.save()
    return redirect('list_sale_orders')

def complete_sale_order(request, id):
    sale_order = get_object_or_404(SaleOrder, id=id)
    if sale_order.status == 'Pending':
        sale_order.status = 'Completed'
        sale_order.save()
    return redirect('list_sale_orders')

from .models import StockMovement
from .forms import StockMovementForm

def list_stock_movements(request):
    stock_movements = StockMovement.objects.all()
    return render(request, 'inventory/stock_movement_list.html', {'stock_movements': stock_movements})

def add_stock_movement(request):
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            stock_movement = form.save(commit=False)
            if stock_movement.movement_type == "Out" and stock_movement.quantity > stock_movement.product.stock_quantity:
                return render(request, 'inventory/stock_movement_form.html', {
                    'form': form,
                    'error': 'Insufficient stock for this product.',
                })
            stock_movement.product.stock_quantity += stock_movement.quantity if stock_movement.movement_type == "In" else -stock_movement.quantity
            stock_movement.product.save()
            stock_movement.save()
            return redirect('list_stock_movements')
    else:
        form = StockMovementForm()
    return render(request, 'inventory/stock_movement_form.html', {'form': form})

def stock_levels(request):
    products = Product.objects.all()
    return render(request, 'inventory/stock_levels.html', {'products': products})


