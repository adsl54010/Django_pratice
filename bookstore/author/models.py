from django.db import models
from django.contrib import admin

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    tel=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    def __unicode__(self):
        return self.name
    
    class Meta(object):
        db_table="profile"
class profileadmin(admin.ModelAdmin):
    pass

admin.site.register(profile,profileadmin)
        