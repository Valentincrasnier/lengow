from django.db import models

# Create your models here.
class Orders(models.Model):
    marketplace = models.CharField()
    idFlux = models.CharField()
    order_id = models.CharField()
    order_mrid = models.CharField()
    order_refid = models.CharField()
