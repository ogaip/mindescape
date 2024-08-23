from django.urls import path
from . import views as web_views

urlpatterns = [
    path("", web_views.index, name="index"),
    path("index2/", web_views.index2, name="index2"),
]
