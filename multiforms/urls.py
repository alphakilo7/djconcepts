from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from .views import SOFHomeView

app_name = "sof"
urlpatterns = [
    path("", SOFHomeView.as_view(), name="home"),
]
