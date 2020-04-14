from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken')),
    path('', views.get_houses),
    path('create_house', views.create_house),
    path('get_houses_point', views.get_houses_around_specific_point)
]
