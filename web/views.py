from django.shortcuts import render

# Create your views here.


def index(request):
    titulo = "M1ND 3$C4P3"
    return render(request, "web/index.html", {"title": titulo})


def index2(request):
    titulo = "M1ND 3$C4P3"
    return render(request, "web/index2.html", {"title": titulo})
