from django.urls import path
from . import views




















urlpatterns = [
    path("", views.users),
    path("test", views.test),
    path("main/<slug:slug_id>", views.mainpage, name="main"),
    path("sep/<slug:slug_id>", views.separate, name="sep")
]







