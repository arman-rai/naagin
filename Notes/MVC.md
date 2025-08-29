MVC (Model-View-Controller) is a design pattern used for developing web applications. It separates the application logic into three interconnected components:

Model:

Represents the data and the business logic of the application. db
Handles database interactions, such as querying and saving data.
In Django, models are defined as Python classes in models.py and map to database tables.
Example:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

```

View:

Handles the presentation logic and user interface. Logic
In Django, views are Python functions or classes in views.py that process requests and return responses (e.g., HTML, JSON).
Example:
```
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

```

Controller:

Acts as the intermediary between the Model and the View.
In Django, the controller role is handled by the framework itself through the URL dispatcher (urls.py), which maps URLs to views.
Example:
```
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
]

Template:
UI html markups dynamic components
```

Note: Django follows the MTV (Model-Template-View) pattern, which is conceptually similar to MVC:

Model: Same as MVC.
Template: Corresponds to the View in MVC, handling the presentation layer.
View: Corresponds to the Controller in MVC, handling the logic and request-response cycle.