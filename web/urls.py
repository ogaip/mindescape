from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views as web_views

urlpatterns = [
    path("", web_views.index, name="index"),
    path("nosotros", web_views.nosotros, name="nosotros"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
