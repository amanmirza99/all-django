from django.db import models

# Create your models here.
class items(models.Model):
    name=models.CharField(max_length=120)
    decsription=models.TextField()
    def __str__(self):
        return self.name
