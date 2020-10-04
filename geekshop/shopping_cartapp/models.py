from django.conf import settings
from django.db import models

# Create your models here.
from mainapp.models import Game


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="shopping_cart")
    product = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(verbose_name="quantity", default=0)
    add_time = models.DateTimeField(verbose_name="add time", auto_now_add=True)

