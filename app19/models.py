from django.db import models
# Create your models here.
class mymodel(models.Model):
    Name=models.CharField(max_length=50)
    Sction=models.CharField( max_length=50)
    Rollno=models.BigIntegerField()
    email=models.EmailField(max_length=254)
    join=models.DateTimeField(auto_now=True)
    Conntct=models.IntegerField()

