from django.urls import path
from . import views




















urlpatterns = [
    path("main/<slug:slug_id>", views.mainpage, name="main"),
    path("sep/<slug:slug_id>", views.separate, name="sep")
]







