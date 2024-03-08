from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404  # redirect HttpResponse

from . import models





def mainpage(request, slug_id):
    a = models.Model.objects.all()
    b = models.Model.pub.all()
    c = get_object_or_404(models.Model, pk=slug_id)
    n = 1
    data = {
        "data_2":c,
        "n":n
    }
    return render(request, "mainpageapp/main.html", data)


def separate(request, slug_id):
    h = get_object_or_404(models.Model, pk=slug_id)
    data = {
        "data_1":h
    }
    return render(request, "mainpageapp/sep.html", data)










def users(request):
    all_objects = models.Information.objects.all()
    data = {
        "objects":all_objects
    }
    return render(request, "mainpageapp/users.html", data)




def test(request):
    a = models.Information.objects.all
    data = {
        "data":a
    }
    return render(request, "mainpageapp/test.html", data)






def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> PAGE NOT FOUND <h1>")


