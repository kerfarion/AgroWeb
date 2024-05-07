from django.shortcuts import render, get_object_or_404
from .models import Kind, Category, Product


def product_list(request, kind_slug=None, category_slug=None):
    kind = None
    kinds = Kind.objects.all()
    category = None
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        kind = category.category

    elif kind_slug:
        kind = get_object_or_404(Kind, slug=kind_slug)
        products = products.filter(kind=kind)
        categories = categories.filter(category=kind)

    return render(request, "Catalog/product/list.html", {"kind": kind, "kinds": kinds, "products": products, "categories": categories})


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

