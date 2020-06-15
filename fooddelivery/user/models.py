from django.db import models

# Create your models here.
class registration(models.Model):
    id =  models.CharField(auto_created = True, primary_key = True,max_length=20)
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'registration'
