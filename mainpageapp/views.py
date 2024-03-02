from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404  # redirect HttpResponse





def mainpage(request, slug_id):
    data = slug_id
    return render(request, "main.html", context=data)






















def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> PAGE NOT FOUND <h1>")


