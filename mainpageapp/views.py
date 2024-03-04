from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404  # redirect HttpResponse

from . import models


def test(request):
    return render(request, "mainpageapp/test.html")

def mainpage(request, slug_id):
    a = models.Model.objects.all()
    b = models.Model.pub.all()
    data = {
        "data_2":b
    }
    return render(request, "mainpageapp/main.html", data)


def separate(request, slug_id):
    h = get_object_or_404(models.Model, slug=slug_id)
    data = {
        "data_1":h
    }
    return render(request, "mainpageapp/sep.html", data)






















def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> PAGE NOT FOUND <h1>")


