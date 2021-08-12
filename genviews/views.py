from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductCreateForm, ProductUpdateForm


class ProductList(ListView):
    """List all products"""
    model = Product
    template_name = "genviews/products.html"
    context_object_name = "products"
    paginate_by = 3

    def get_queryset(self):
        sort_mapping = {
            "price": ["price", "id"],
            "priced": ["-price", "id"],
            "title": ["title", "id"],
            "titled": ["-title", "id"],
            "id": ["id"],
            "idd": ["-id"],
        }
        search_term = self.request.GET.get("q")
        sort_term = self.request.GET.get("sort")
        sort_term = sort_mapping.get(sort_term, ["id"])
        objects_all = self.model.objects.all().order_by(*sort_term)
        if search_term:
            objects_all = objects_all.filter(Q(title__contains=search_term) |
                                             Q(tagline__contains=search_term))\
                                     .order_by(*sort_term)

        return objects_all


class ProductDetail(DetailView):

    model = Product
    template_name = "genviews/product_detail.html"
    context_object_name = "product"

    def get_object(self):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=product_id)


class ProductCreate(CreateView):

    form_class = ProductCreateForm
    template_name = "genviews/product_create.html"
    success_url = reverse_lazy("products:view_all")


class ProductUpdate(UpdateView):

    model = Product
    form_class = ProductUpdateForm
    template_name = "genviews/product_update.html"
    context_object_name = "product"
    success_url = reverse_lazy("products:view_all")

    def get_object(self):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=product_id)


class ProductDelete(DeleteView):

    model = Product
    template_name = "genviews/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("products:view_all")

    def get_object(self):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=product_id)
