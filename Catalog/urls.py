from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('filter/<slug:kind_slug>', views.product_list, name="product_list_by_kind"),
    path('filter/<slug:kind_slug>/<slug:category_slug>', views.product_list, name="product_list_by_category"),
    path('filter/<int:id>/<slug:category_slug>', views.product_detail, name="products_detail"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts")
]