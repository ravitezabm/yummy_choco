from django.db import models

# Create your models here.
class reg_tbl(models.Model):
    fn = models.CharField(max_length=50)
    mb = models.IntegerField()
    em = models.EmailField()
    ps = models.CharField(max_length=50)
    def __str__(self):
        return self.fn
    
class choco_tbl(models.Model):
    cnm=models.CharField(max_length=40)
    cpic=models.FileField(upload_to="pictures")
    cprc=models.IntegerField()
    def __str__(self):
        return self.cnm