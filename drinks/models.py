from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)


    def __str__(self):
        data = f"name: {self.name}, description: {self.description}"
        return data