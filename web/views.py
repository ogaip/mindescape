from django.shortcuts import render

# Create your views here.


def index(request):
    titulo = "M1ND 3$C4P3"
    return render(request, "web/medialab/index.html")

def nosotros(request):
    print(request.user)
    return render(request, "web/medialab/index.html")
