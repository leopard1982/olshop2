from django.db import models

# Create your models here.
class searchKeyword(models.Model):
    keyword = models.CharField(max_length=50, primary_key=True,null=False,blank=False,default="")
    jumlah = models.IntegerField(default=0)

    class Meta:
        ordering = ['-jumlah']