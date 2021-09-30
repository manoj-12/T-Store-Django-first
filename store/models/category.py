from django.db import models

class Cotegory(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category