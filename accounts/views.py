from datetime import datetime

from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse


# Create your views here.
def api_home(request):
    return JsonResponse({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                         "message": "welcome!"})
