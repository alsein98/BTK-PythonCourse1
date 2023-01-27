import random
num=random.randint(0,100)

hak=5

while hak>0:
    hak-=1
    tahmin=int(input("enter a num "))
    if tahmin == num:
        print("tebrikler")
        break
    elif tahmin<num:
        print("yukari")
    else:
        print("aşaği")
    if hak==0:
        print("hakkiniz bitti")
        print(f"sayi {num} idi")