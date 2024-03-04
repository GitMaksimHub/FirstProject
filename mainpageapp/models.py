from django.db import models
from django.urls import reverse


#python manage.py makemigrations
#python manage.py sqlmigrate mainpageapp 0004
#python manage.py migrate


#python manage.py shell
#from mainpage.models import Classname


class Pub(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(second=0)

class Model(models.Model):
    first = models.CharField(max_length=20, default="")
    second = models.BooleanField(default=True)
    slug = models.SlugField(default="", max_length=30, blank=True)
    key = models.ForeignKey("Foreg", on_delete=models.CASCADE)
    objects = models.Manager()
    pub = Pub()
    def get_absolute_url(self):
        return reverse("sep", kwargs={"slug_id":self.slug})

class Foreg(models.Model):
    worker = models.BooleanField(default=False)
    non_worker = models.BooleanField(default=False)















