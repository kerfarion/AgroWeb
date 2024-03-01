from django.shortcuts import render, get_object_or_404
from .models import Kind, Category, Product


def product_list(request, kind_slug=None, category_slug=None):
    kind = None
    kinds = Kind.objects.all()
    category = None
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True)
    if kind_slug:
        kind = get_object_or_404(Kind, slug=kind_slug)
        products = products.filter(kind=kind)

    return render(request, "Catalog/product/list.html", {"kind": kind, "kinds": kinds, "products": products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'Catalog/products/details.html',
                  {"product": product})


def contacts(request):
    return render(request, 'Catalog/contacts.html')


def about(request):
    return render(request, "Catalog/about.html")

