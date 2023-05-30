from django.db import models
from users.models import CustomUser

class Listing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # other fields can be added here
