from django.db import models
from django.core.validators import MaxValueValidator,  MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save,  sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,  instance=None,  created=False,  **kwargs):
    if created:
        Token.objects.create(user=instance)

CATEGORY_CHOICES = ((1,  'Gastronomie'), 
                                        (2,  'Lebensmittel'), 
                                        (3,  'Elektronik'), 
                                        (4,  'Textil/Fashion'),
                                        (5, 'Fahrzeug'),
                                        (6,  'Schmuck'), 
                                        (7,  'Fitness/Sport'),
                                       (8, 'Beauty/Wellness'),  
                                       (9, 'Abenteuer/Freizeit'), 
                                       (10, 'Bildung'), 
                                       (11, 'Diverses'))

class Task(models.Model):
    name = models.CharField(max_length=100,  default='Shopname')
    description = models.TextField(max_length=200,  default='description')
    category = models.IntegerField(choices=CATEGORY_CHOICES,  default=1)
    pictures = models.ImageField(upload_to='uploads/',  default='uploads/fail.jpg')
    coordinatesx = models.FloatField( default = 0)
    coordinatesy = models.FloatField( default = 0)
    rating = models.IntegerField(default=1,  validators=[MaxValueValidator(5),  MinValueValidator(1)])
    date_created =models.DateTimeField(auto_now=True)
    
    def ___str__(self):
        return "%s" % self.name
        
