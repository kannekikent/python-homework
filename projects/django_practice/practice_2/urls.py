"""Маршрут страницы с фотографиями собак."""

from django.urls import path
from views import dogs

urlpatterns = [
    path("", dogs),
]
