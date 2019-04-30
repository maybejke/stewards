from django.db import models

# Create your models here.


class UserContact(models.Model):
    subject = models.CharField(verbose_name='титул', max_length=64, default='Anketa')
    full_name = models.CharField(verbose_name='имя', max_length=64,unique=True)
    age = models.IntegerField(verbose_name='возраст', default=18)
    phone_number = models.CharField(verbose_name='телефон', max_length=64, blank=True)
    city = models.CharField(verbose_name='город', max_length=64, blank=True)
    about = models.TextField(verbose_name='описание', max_length=64, blank=True)
    sender = models.EmailField(verbose_name='email', max_length=254)

    def __str__(self):
        return self.name