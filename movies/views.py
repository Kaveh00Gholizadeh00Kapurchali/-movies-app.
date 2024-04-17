from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    context = {
        "movies": ["gladiator", "sefid barfi", "jojo", "starwars"]
    }
    return render(request, "movies/index.html", context)

def about_me(request):
    return render(request, "movies/about_me.html", {})