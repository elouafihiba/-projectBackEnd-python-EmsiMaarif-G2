from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pets(models.Model):
    nom = models.CharField(max_length = 100)
    prenom = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)
    descr = models.CharField(max_length = 10000, null = True)
    is_adopt = models.BooleanField(default=False)
    datecreation = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)


    def __str___(self):
        return self.prenom