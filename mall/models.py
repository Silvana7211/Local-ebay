from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db.models import Max


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    upc = models.CharField(max_length=50)
    condition = models.IntegerField(
        choices=(('1', 'New'), ('2', 'Open Box'), ('3', 'Certified refurbished'), ('4', 'Used')))
    brand = models.CharField(max_length=30)
    description = models.TextField()
    starting_price = models.FloatField()
    deadline = models.DateTimeField()
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def bids(self):
        return self.bid_set.all()

    @property
    def max_bid(self):
        return self.bid_set.all().aggregate(max_bid=Max('value'), buyer=Max('placer'))


class Bid(models.Model):
    value = models.FloatField()
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    product = models.ForeignKey('mall.Product', on_delete=models.CASCADE)
    placer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %f' % (self.placer.username, self.value)
