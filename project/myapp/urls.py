from django.urls import path
from . import views

urlpatterns = [
    path("function", views.say_hello),
    path("Class", views.Hello.as_view()),
    path("home", views.home),
    path("", views.home),
    path("reservation", views.home, name="reservation"),
]