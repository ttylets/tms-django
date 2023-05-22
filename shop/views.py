from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect


from .models import Category, Product, Order, OrderEntry


def categories_view(request):
    return render(request, 'shop/index.html', {
        'categories': Category.objects.all(),
    })


def category_detail(request, category_id: int):
    return render(request, 'shop/category_detail.html', {
        'category': get_object_or_404(Category, id=category_id),
    })


def products_view(request):
    return render(request, 'shop/products.html', {
        'products': Product.objects.all(),
    })


def product_detail(request, product_id: int):
    return render(request, 'shop/product_detail.html', {
        'product': get_object_or_404(Product, id=product_id),
    })


@login_required
def add_to_cart(request: HttpRequest):
    profile = request.user.profile
    if not request.user.profile.shopping_cart:
        request.user.profile.shopping_cart = Order(profile=request.user.profile)
        request.user.profile.shopping_cart.save()

    assert request.method == 'POST'
    product_id = request.POST['product_id']
    product = get_object_or_404(Product, id=product_id)

    order_entry = OrderEntry.objects.filter(product=product, order=profile.shopping_cart).first()
    if not order_entry:
        order_entry = profile.shopping_cart.order_entries.create(product=product, count=0)
    order_entry.count += 1
    order_entry.save()
    return redirect('shop:product_detail', product_id)







