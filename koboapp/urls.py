from django.urls import path
from . import views


urlpatterns = [
    path('store_data/',views.store_data,name='store_data'),
]