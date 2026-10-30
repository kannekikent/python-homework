"""Шифрование и расшифровка текста шифром Цезаря."""

import string

print("Введите текст построчно (после каждой введенной строки: Enter)")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
text = " ".join(lines)
lang = input("Выберите язык (eng/rus): ")
key = input("Введите ключ: ")
tpy = input("Зашифровать/расшифровать: ")
key = int(key)
tpy = tpy.lower()
stxt = text
text = text.lower()
text = (
    text.replace(" ", "")
    .replace(",", "")
    .replace(".", "")
    .replace("!", "")
    .replace("?", "")
    .replace(":", "")
)


def cipher(text, key, tpy, lang):
    """Вернуть текст со сдвигом букв выбранного алфавита на ключ."""
    desc = ""
    if lang == "eng":
        alph = string.ascii_lowercase
        if tpy == "зашифровать":
            for i in text:
                ind = alph.index(i)
                mth = (ind + key) % len(alph)
                desc = desc + alph[mth]
            return desc
        else:
            for i in text:
                ind = alph.index(i)
                mth = ind - key
                desc = desc + alph[mth]
            return desc
    else:
        alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        if tpy == "зашифровать":
            for i in text:
                ind = alph.index(i)
                mth = (ind + key) % len(alph)
                desc = desc + alph[mth]
            return desc
        else:
            for i in text:
                ind = alph.index(i)
                mth = ind - key
                desc = desc + alph[mth]
            return desc


print(stxt)
print(cipher(text, key, tpy, lang))
