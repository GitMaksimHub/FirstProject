from django.db import models
from django.urls import reverse


#python manage.py makemigrations
#python manage.py sqlmigrate mainpageapp 0004
#python manage.py migrate


#python manage.py shell
#from mainpage.models import Classname






class Worker_or_lazy(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(foreign_id=Model.Custom_Choices.worker)



class Model(models.Model):
    class Custom_Choices(models.IntegerChoices):
        worker = 1, "worker"
        lazy = 2, "lazy"
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    foreign = models.ForeignKey("Categorys", on_delete=models.CASCADE)
    objects = models.Manager()
    work_or_laz = Worker_or_lazy()
    worker_or_not = models.BooleanField(choices=Custom_Choices.choices, default=Custom_Choices.worker)
    def __str__(self):
        return self.name
    def get_object_or_404(self):
        return reverse("waytwo", kwargs={"slug_id":self.slug})

class Categorys(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name















