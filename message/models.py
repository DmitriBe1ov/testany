from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=256)
    second_name = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name, self.second_name


