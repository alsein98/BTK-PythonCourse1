# loops
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# 1-
for s in sayilar:
    print(f"{s} 3'un katidir : ", s % 3 == 0)
for s in sayilar:
    if (s % 3 == 0):
        print(s)
# 2-
print(sum(sayilar))
summ = 0
for s in sayilar:
    summ += s
print(summ)
# 3-
for s in sayilar:
    if s % 2 != 0:
        print(s**2)

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]
# 4-
for s in sehirler:
    print(s, "en fazla 5 karakterlidir :", len(s) <= 5)
for s in sehirler:
    if len(s) <= 5:
        print(s)

urunlar = [
    {"name": "samsung S6", "price": "3000"},
    {"name": "samsung S7", "price": "4000"},
    {"name": "samsung S8", "price": "5000"},
    {"name": "samsung S9", "price": "6000"},
    {"name": "samsung S10", "price": "7000"}
]
# 5-
total = 0
for v in urunlar:
    total += int(v["price"])
print(total)

# 6-
for u in urunlar:
    if int(u["price"])<=5000:
        print(u["name"])