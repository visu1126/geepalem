from django.db import models

class goods(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField()
    item_cost=models.DecimalField(max_digits=10, decimal_places=2)
    stock_qty=models.DecimalField(max_digits=10, decimal_places=2)
    volume=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def product(self):
        v=self.item_cost * self.stock_qty
        return v

    def save(self):
        self.volume = self.product()
        super(goods, self).save()

    def __str__(self):
        return self.name
