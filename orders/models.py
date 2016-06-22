from django.db import models



# Create your models here.
class Order(models.Model):
    marketplace = models.TextField()
    idFlux = models.TextField()
    order_id = models.TextField()
    order_mrid = models.TextField()