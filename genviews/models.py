from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    title = models.CharField(_("Product Title"), max_length=64)
    tagline = models.CharField(_("Tag Line"), max_length=256)
    price = models.FloatField(_("Price"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:view_one", kwargs={"pk": self.id})
