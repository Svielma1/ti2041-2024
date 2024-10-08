from django.db import models
from django.utils import timezone

# Create your models here.
class Common_info(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", help_text="Obligatorio")
    class Meta:
        abstract: True

    def __str__(self):
        return self.name

class Category(Common_info):
    id_category = models.AutoField(primary_key=True)

class Tag(Common_info):
    id_tag = models.AutoField(primary_key=True)

class Post(models.Model):
    AUTHORS = {
        "AMO": "Andrés Muñoz Órdenes",
        "VAF": "Verónica Astorga Figueroa",
        "JPC": "Juan Pérez Cotapos",
    }
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    author = models.CharField(max_length=3, choices=AUTHORS)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    publish_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title + " (" + self.author + ")"