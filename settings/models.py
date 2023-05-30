from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser

class Settings(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    payment_policy = models.TextField()
    shipping_policy = models.TextField()
    return_policy = models.TextField()
    # other fields can be added here
