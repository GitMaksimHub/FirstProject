from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404  # redirect HttpResponse

from .models import Model
def wayone(request):
    info = Model.work_or_laz.all()
    data = {"data":info}
    return render(request, "mainpageapp/wayone.html", data)


def waytwo(request, slug_id):
    info = get_object_or_404(Model, slug=slug_id)
    data = {"data":info}
    return render(request, "mainpageapp/waytwo.html", data)


























def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> PAGE NOT FOUND <h1>")


