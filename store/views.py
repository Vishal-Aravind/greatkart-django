from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):    #None means not necessary field
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()

    else:
        products =Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,         # generally views prepare the data to be shown in the screen and gives it to the store.html
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)  #category__slug, double underscore is used for accessing the slug inside category models
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)