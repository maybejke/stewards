from django.db import models

# Create your models here.

class EventCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64,unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активная категория', default=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя мероприятия', max_length=128)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    short_desc = models.CharField(verbose_name='краткое описание мероприятия', max_length=60, blank=True, null=True)
    description = models.TextField(verbose_name='описание мероприятия', blank=True, null=True)
    timeofevent = models.CharField(verbose_name='дата мероприятия', max_length=60, blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name='количество зрителей', default=0, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='активная категория', default=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)


class Document(models.Model):
    name = models.CharField(verbose_name='имя документа', max_length=128)
    file = models.FileField(upload_to='pdf/', blank=True, null=True)
    short_desc = models.CharField(verbose_name='краткое описание Документа', max_length=60, blank=True, null=True)
    description = models.TextField(verbose_name='описание Документа', blank=True, null=True)

    def __str__(self):
        return self.name