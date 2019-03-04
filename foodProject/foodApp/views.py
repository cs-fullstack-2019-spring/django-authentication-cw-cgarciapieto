from django.shortcuts import render
from django.http import HttpResponse
from .forms import FoodForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return HttpResponse("Test URL")

# pulls the model and creates and renders a form on page
def newForm(request):

    form = FoodForm(request.POST or None)
    context = {
        "form": form
    }
    return render('foodApp/fitness.html', context)

# post and creates a user in the database
def newPost(request):
    if request.method == "POST":
        User.objects.create_user(request.POST["username"], request.POST["password"], request.POST['calories'],
                                 request.POST['date'])
        return render(request, "foodApp/fitness.html")

    return render(request, 'foodApp/fitness.html')
