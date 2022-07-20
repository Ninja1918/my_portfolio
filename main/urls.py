from django.urls import path, include
from main.views import index, about, certifications


urlpatterns = [
    path('', index.as_view(), name = 'indexPage'),
    path('about', about.as_view(), name = 'aboutPage'),
    path('certification', certifications.as_view(), name = 'certificationPage')
]
