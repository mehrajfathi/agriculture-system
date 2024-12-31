from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order
from .forms import ProductForm

def marketplace(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'marketplace/marketplace.html', {
        'products': products,
        'title': 'Marketplace'
    })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('marketplace:marketplace')
    else:
        form = ProductForm()
    
    return render(request, 'marketplace/product_form.html', {
        'form': form,
        'title': 'Add Product'
    })

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('marketplace:marketplace')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'marketplace/product_form.html', {
        'form': form,
        'product': product,
        'title': 'Edit Product'
    })

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('marketplace:marketplace')
    
    return render(request, 'marketplace/delete_product.html', {
        'product': product,
        'title': 'Delete Product'
    })

@login_required
def my_products(request):
    products = Product.objects.filter(seller=request.user).order_by('-created_at')
    return render(request, 'marketplace/my_products.html', {
        'products': products,
        'title': 'My Products'
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'marketplace/product_detail.html', {
        'product': product,
        'title': product.title
    })

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user != order.buyer and request.user != order.product.seller:
        messages.error(request, "You don't have permission to view this order.")
        return redirect('marketplace:marketplace')
    return render(request, 'marketplace/order_detail.html', {
        'order': order,
        'title': f'Order #{order.id} Details'
    })

@login_required
def my_orders(request):
    orders = Order.objects.filter(buyer=request.user).order_by('-created_at')
    return render(request, 'marketplace/my_orders.html', {
        'orders': orders,
        'title': 'My Orders'
    })

@login_required
def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.seller == request.user:
        messages.error(request, "You cannot buy your own product!")
        return redirect('marketplace:product_detail', pk=pk)
    
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
                
            if quantity <= product.quantity:
                order = Order.objects.create(
                    buyer=request.user,
                    product=product,
                    quantity=quantity,
                    total_price=product.price * quantity
                )
                product.quantity -= quantity
                product.save()
                messages.success(request, 'Order placed successfully!')
                return redirect('marketplace:order_detail', order_id=order.id)
            else:
                messages.error(request, 'Not enough quantity available!')
        except ValueError:
            messages.error(request, 'Invalid quantity specified!')
    
    return redirect('marketplace:product_detail', pk=pk)
