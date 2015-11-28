from django.db import models
from django.utils import timezone
from django.db.models import Sum


class Food(models.Model):

    """
    Food object
    """
    name = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Food, self).save(*args, **kwargs)


class Customer(models.Model):
    gender = (('M', 'Male'), ('F', 'Female'))
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=gender)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    states = (
        ('D', 'delivered'),
        ('C', "cancelled"),
        ('A', "accepted"),
        ('P', 'draft'),
        )
    customer = models.ForeignKey(Customer)
    amount = models.PositiveIntegerField(default=0)
    details = models.ManyToManyField(
        Food, through="Detail", through_fields=('order', 'food'))
    address = models.CharField("Address", max_length=40)
    status = models.CharField(
        "Order Status", max_length=1, choices=states, default='P'
        )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.pk.__str__()

    def calc_amount(self):
        return Detail.objects.filter(order=self).aggregate(
            Sum('cost')
            )['cost__sum']

    def refresh_amount(self):
        if self.status == 'P':
            pass
        self.amount = self.calc_amount()
        return self.amount

    def save(self, *args, **kwargs):
        if self.status is not 'P':
            # or raise some error
            return
        self.updated = timezone.now()
        self.refresh_amount()
        super(Order, self).save(*args, **kwargs)


class Detail(models.Model):

    """
    every object is particular of common order parent

    plans to update the cost at regular intervals if order in
    draft state for long
    """
    class Meta:
        unique_together = ('order', 'food')

# Ideas:
# it might be better if we save the current value of the food items
# coz its possible to generate reciepts without reverse-
# engineering the rates
# trying this will make amount variable in order class useless 

    food = models.ForeignKey(Food)
    order = models.ForeignKey(Order)
    quantity = models.PositiveIntegerField()
    cost = models.PositiveIntegerField(default=0)

    def calc_cost(self):
        return self.food.cost * self.quantity

    def __str__(self):
        return "{0} {1}".format(self.order, self.food)

    def save(self, *args, **kwargs):
        self.cost = self.calc_cost()
        super(Detail, self).save(*args, **kwargs)
