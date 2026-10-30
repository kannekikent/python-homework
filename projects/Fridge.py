"""Учёт партий продуктов и их сроков годности в холодильнике."""

from datetime import date, datetime
from decimal import Decimal

DATE_FORMAT = "%Y-%m-%d"

goods = {}


def add(items, title, amount, expiration_date=None):
    """Добавить продукт или новую партию в холодильник."""
    if isinstance(expiration_date, str):
        expiration_date = datetime.strptime(
            expiration_date,
            DATE_FORMAT,
        ).date()

    product = {
        "amount": Decimal(str(amount)),
        "expiration_date": expiration_date,
    }

    if title not in items:
        items[title] = []

    items[title].append(product)


def add_by_note(items, note):
    """Добавить продукт по текстовой записи."""
    parts = note.split()
    expiration_date = None

    try:
        expiration_date = datetime.strptime(
            parts[-1],
            DATE_FORMAT,
        ).date()
        parts.pop()
    except ValueError:
        pass

    amount_value = Decimal(parts.pop())
    title = " ".join(parts)

    add(items, title, amount_value, expiration_date)


def find(items, needle):
    """Найти продукты, содержащие указанную строку."""
    result = []

    for title in items:
        if needle.lower() in title.lower():
            result.append(title)

    return result


def amount(items, title):
    """Посчитать количество непросроченного продукта."""
    total = Decimal("0")
    today = date.today()

    if title not in items:
        return total

    for product in items[title]:
        expiration_date = product["expiration_date"]

        if expiration_date is None or expiration_date >= today:
            total += product["amount"]

    return total


add(goods, "Молоко", 2)
add(goods, "Яйца", 10)
add(goods, "Сыр", Decimal("0.5"))

add_by_note(goods, "Макароны 3 2030-12-31")
add_by_note(goods, "Молоко 1 2030-10-20")

print("=== СОДЕРЖИМОЕ ХОЛОДИЛЬНИКА ===")

for title in goods:
    print(f"{title}: {amount(goods, title)} шт.")

print("\n=== ПОИСК ПРОДУКТОВ ===")

for title in find(goods, "мол"):
    print(f"По запросу 'мол': {title} — {amount(goods, title)} шт.")
