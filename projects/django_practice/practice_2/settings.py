"""Настройки страницы с фотографиями собак."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = "django-insecure-local-dog-api-practice"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
    },
]
