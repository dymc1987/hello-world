from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=5,primary_key=True)
    department = models.CharField(max_length=10)
    job_position = models.CharField(max_length=20)


class Pc_assets(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    pc_type = models.CharField(max_length=20)
    sn = models.CharField(max_length=10,unique=True)
    assets_num = models.IntegerField(max_length=15,unique=True,null=True)

