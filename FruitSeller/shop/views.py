from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from cart.forms import CartAddProductForm
from .models import Category, Product


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html', {
            'category': category,
            'categories': categories,
            'products': products
        })


def detail_product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
