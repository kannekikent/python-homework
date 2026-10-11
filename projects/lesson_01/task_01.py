"""Домашние задания по Python."""
print("1 задание")
tmp_cel = 15
tmp_fer = (tmp_cel*9/5)+32
tmp_kel = (tmp_cel+273.15)
print(tmp_fer)
print(tmp_kel)





print("2 задание")
a = int(input())
if a % 2 == 0:
    print("чётное")
else:
    print("не чётное")
if a > 0:
    print("положительное")
elif a == 0:
    print(0)
else:
    print("отрицательное")
if 10 <= a <= 50:
    print("да")
else:
    print("нет")






print("3 задание")
import random
import string


letters = random.choices(string.ascii_uppercase, k=3)
digits = random.choices(string.digits, k=3)
specials = random.choices("!@#$%^&*", k=2)

password_list = letters + digits + specials
random.shuffle(password_list)
print("".join(password_list))


print("4 задание")
a = input().lower()
kol_sim = {}
for i in a:
    if i in kol_sim:
        kol_sim[i] += 1
    else:
        kol_sim[i] = 1
kol1 = []
for i in kol_sim:
    kol1.append((kol_sim[i], i))
kol1 = sorted(kol1)
print(kol1[-1][1], kol1[-2][1], kol1[-3][1])



print("5 задание")
n = int(input())
num = [i for i in range(2, n + 1)]
i = 2
ind = 0
while True:
    num = [j for j in num if j % i != 0 or j == i]
    ind += 1
    if ind == len(num):
        break
    i = num[ind]
print(num)

