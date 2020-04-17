from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken')),
    path('all_houses', views.get_houses),
    path('all_houses/point', views.get_houses_around_specific_point),
    path('create_house', views.create_house),
    path('house_images', views.house_image)
]
