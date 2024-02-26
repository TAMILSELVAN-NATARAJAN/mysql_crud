from django.db import models

# Create your models here.
class Employee(models.Model):
    name =models.CharField(max_length=100)
    email =models.EmailField()
    password =models.CharField(max_length=100)

    class Meta :
        db_table ="table_client"

   