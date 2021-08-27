from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from core.models import Product


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bids')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_bids')
    amount = models.DecimalField(_('Amount'), max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(_('Created At'), auto_now=True)

    def __str__(self):
        return '%s-%s: %s' % (self.user.username, self.product.name, self.amount)


class AutoBidConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_auto_bids')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_auto_bids')
    increment = models.DecimalField(_('Increment Amount'), max_digits=100, decimal_places=2)
    max_amount = models.DecimalField(_('Maximum Amount'), max_digits=100, decimal_places=2)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = 'Auto Bid Configuration'

    def __str__(self):
        return '%s-%s' % (self.user.username, self.product.name)
