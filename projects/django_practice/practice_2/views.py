"""Запросы к Dog API и подготовка данных для шаблона."""

import json
from urllib.error import URLError
from urllib.request import urlopen

from django.shortcuts import render

API_URL = "https://dog.ceo/api/"


def get_breeds():
    """Получить список пород собак."""
    with urlopen(API_URL + "breeds/list/all", timeout=10) as response:
        return sorted(json.load(response)["message"])


def get_photo(breed):
    """Получить ссылку на случайную фотографию породы."""
    url = API_URL + f"breed/{breed}/images/random"
    with urlopen(url, timeout=10) as response:
        return json.load(response)["message"]


def dogs(request):
    """Показать список пород и фотографии выбранных собак."""
    query = request.GET.get("breeds", "")
    breeds = []
    photos = []
    errors = []

    try:
        breeds = get_breeds()
    except (URLError, TimeoutError):
        errors.append("Не удалось загрузить список пород.")

    if breeds:
        for name in query.split(","):
            breed = name.strip().lower()
            if not breed:
                continue
            if breed not in breeds:
                errors.append(f"Порода не найдена: {breed}")
                continue

            try:
                photo = get_photo(breed)
                photos.append({"breed": breed, "url": photo})
            except (URLError, TimeoutError):
                errors.append(f"Не удалось загрузить фото породы {breed}.")

    return render(
        request,
        "dogs.html",
        {
            "breeds": breeds,
            "photos": photos,
            "errors": errors,
            "query": query,
        },
    )
