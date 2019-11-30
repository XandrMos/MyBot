from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=250)

    def __str__(self):
        return self.user_id