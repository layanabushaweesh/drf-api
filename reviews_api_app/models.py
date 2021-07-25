from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
# Create your models here.

class Reviews(models.Model):

    item = models.CharField(max_length=64)
    review = models.TextField()
    purchaser= models.ForeignKey(get_user_model(), on_delete=CASCADE)
    
    def __str__(self):
        return self.item