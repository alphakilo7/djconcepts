from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView


# Create your views here.
class SOFHomeView(TemplateView):
    template_name = "multiforms/sofhome.html"
