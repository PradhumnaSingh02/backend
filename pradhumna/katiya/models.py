from django.db import models

class login(models.Model):
    name = models.CharField(max_length=120)
    enrollement_no = models.TextField()


    def __str__(self):
        return self.name