from django.urls import path
from . import views




















urlpatterns = [
    path("wayone", views.wayone, name="wayone"),
    #path("waytwo/<slug:slug_id>", views.waytwo, name="waytwo")
]







