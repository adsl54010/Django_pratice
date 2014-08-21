from django.db import models
from author.models import profile
from django.contrib import admin

class Book(models.Model):
    title=models.CharField(max_length=150)
    page=models.IntegerField()
    price=models.IntegerField()
    author=models.ForeignKey(profile)
    publish_date=models.DateField()
    
    class Meta(object):
        db_table="book"
        
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book,BookAdmin)