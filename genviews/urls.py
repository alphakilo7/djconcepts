from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from .views import ProductList, ProductDetail, ProductCreate
from .views import ProductUpdate, ProductDelete


app_name = "products"
urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("products:view_all")), name="home"),
    path("_all/", ProductList.as_view(), name="view_all"),
    path("view/<int:id>/", ProductDetail.as_view(), name="view_one"),
    path("create/", ProductCreate.as_view(), name="create"),
    path("update/<int:id>/", ProductUpdate.as_view(), name="update"),
    path("delete/<int:id>/", ProductDelete.as_view(), name="delete"),
]
