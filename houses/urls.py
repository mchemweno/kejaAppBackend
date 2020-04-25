from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken')),
    # "Users endpoints
    path('users', views.user_list),
    path('users/email/<str:email>', views.user_detail_email),
    path('users/<int:id>', views.user_detail_id),
    # activation and password reset urls
    path('users/activate/<str:uid>/<str:token>', views.activation),
    path('users/password-reset/<str:uid>/<str:token>', views.reset),
    # houses endpoints APIs
    path('all_houses', views.get_houses),
    path('all_houses/point', views.get_houses_around_specific_point),
    path('create_house', views.create_house),
    path('house_images', views.house_image)
]
