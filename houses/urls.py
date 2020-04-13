from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.get_houses),
                  path('create_house', views.create_house)
              ]