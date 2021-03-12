from django.db import models

class Emloeer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    contact = models.CharField(max_length=15)


    class Meta:
        db_table = 'employee'



