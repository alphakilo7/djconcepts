from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from django.urls import reverse_lazy

from accounts.views import api_home, LoginView, LogoutView, RegisterView


app_name = "accounts"
urlpatterns = [
    path("", TemplateView.as_view(template_name="accounts/home.html"), name="home"),
    path("accounts/", RedirectView.as_view(url=reverse_lazy("accounts:home")), name="base"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
]
