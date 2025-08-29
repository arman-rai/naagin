from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Home view
def home(request):
    form = ReservationForm()
    if request.method == "POST":  # Fix case sensitivity for HTTP method
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success, form saved in the db")
    return render(request, 'index.html', {'form': form})

# Create your views here.

def say_hello(request):
    return HttpResponse("hello from a function.")

# Class based

class Hello(View):
    def get(self, request):
        return HttpResponse("Hello using class.")
