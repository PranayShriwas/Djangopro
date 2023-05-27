from django.db import models

# Create your models here.
class Emp(models.Model):
    Ename=models.CharField( max_length=50)
    Email=models.EmailField( max_length=54)
    Mobile_no=models.IntegerField()
    Address=models.TextField()
    Joining_date=models.DateField()
    def __str__(self) -> str:
        return self.Ename