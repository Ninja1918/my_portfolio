from django.urls import path, include
from main.views import index


urlpatterns = [
    path('', index.as_view(), name = 'index')
]