from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=5,primary_key=True)
    # 设置了name为主键，就不会创建数据表的id字段。如果这里不指定某一
    # 字段为主键，则会自动创建id字段，作为主键
    department = models.CharField(max_length=10)
    job_position = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pc_assets(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    pc_type = models.CharField(max_length=20)
    sn = models.CharField(max_length=10,unique=True)
    assets_num = models.IntegerField(unique=True,null=True)

