from datetime import datetime

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from accounts.forms import RegistrationForm


# Create your views here.
def api_home(request):
    return JsonResponse({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                         "message": "welcome!"})


class RegisterView(CreateView):
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")
    form_class = RegistrationForm


class LoginView(BaseLoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class LogoutView(BaseLogoutView):
    template_name = "accounts/logout.html"

