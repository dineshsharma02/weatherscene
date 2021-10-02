
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('delete-city/<city_name>/',views.delete_city,name='delete_city'),
]
