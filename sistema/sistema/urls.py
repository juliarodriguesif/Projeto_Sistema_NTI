from django.contrib import admin
from django.urls import path
from sistema.core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),       #irá aparecer o conteúdo que está na página home.html
]
