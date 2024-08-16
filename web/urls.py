
from django.urls import path
from . import views as web_views

urlpatterns = [
    
    path('', web_views.index, name="index"),

]
