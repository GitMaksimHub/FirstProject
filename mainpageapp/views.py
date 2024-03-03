from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404  # redirect HttpResponse

from . import models




def mainpage(request, slug_id):
    a = models.Model.objects.all()
    data = {
        "data_1":slug_id,
        "data_2":a
    }
    return render(request, "mainpageapp/main.html", data)


def separate(request, slug_id):
    h = get_object_or_404(models.Model, first=slug_id)
    data = {
        "data_1":h.first,
        "data_2":h.second,
        "data_3":h.key_id
    }
    return render(request, "mainpageapp/sep.html", data)






















def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> PAGE NOT FOUND <h1>")


