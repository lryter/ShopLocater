from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100,  default='nothing')
    description = models.TextField(max_length=200,  default='nothing')
    pictures = models.ImageField(upload_to='uploads/',  default='uploads/fail.jpg')
    coordinatesx = models.FloatField( default = 0)
    coordinatesy = models.FloatField( default = 0)
    date_created =models.DateTimeField(auto_now=True)
    
    def ___str__(self):
        return "%s" % self.name
        
