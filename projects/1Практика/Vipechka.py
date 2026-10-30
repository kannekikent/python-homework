"""Выбор фасовки выпечки по количеству изделий."""


def print_pack_report(d):
    """Вернуть описание подходящей фасовки для количества изделий."""
    if d % 3 == 0 or d % 5 == 0:
        if d % 3 == 0 and d % 5 == 0:
            return str(d) + " - " + "расфасуем по 3 или по 5"
        if d % 3 == 0:
            return str(d) + " - " + "расфасуем по 3"
        if d % 5 == 0:
            return str(d) + " - " + "расфасуем по 5"
    else:
        return str(d) + " - " + "не заказываем!"


pir = 10
rzh = 13
rip = 30
print(print_pack_report(pir))
print(print_pack_report(rzh))
print(print_pack_report(rip))
