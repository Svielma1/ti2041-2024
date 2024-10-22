from django.db import models

# Create your models here.
class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text="Obligatorio")
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Characteristics(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    color = models.CharField(max_length=50, default="Por definir")

class Product(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    characteristics = models.ManyToManyField(Characteristics, through="Data")

    def __str__(self):
        return self.name

class Data(models.Model):
    characteristics = models.ForeignKey(Characteristics, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)