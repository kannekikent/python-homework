"""Калькулятор с четырьмя арифметическими операциями."""


def calculator(a, b, op):
    """Выполнить арифметическую операцию над двумя числами."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Нельзя делить на ноль"
        if a % b == 0:
            return int(a / b)
        else:
            return a / b
    else:
        return "Неизвестная операция"


a = float(input("Введите первое число: "))
op = input("Введите знак (+, -, *, /): ")
b = float(input("Введите второе число: "))
print(calculator(a, b, op))
