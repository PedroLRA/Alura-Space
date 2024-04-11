from django.urls import path
from galery.views import index

urlpatterns = [
    path('', index)
]
